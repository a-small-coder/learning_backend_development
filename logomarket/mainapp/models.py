from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.urls import reverse

User = get_user_model()


def get_product_url(obj, view_name):
    ct_model = obj.__class__.meta.model_name
    return reverse(view_name, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model_in=args)
        for ct_model in ct_models:
            model_product = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_product)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    object = LatestProductsManager


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{}: {}".format(self.category, self.name)


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    main_image = models.ImageField(verbose_name='Изображение')
    sub_images = GenericRelation('subimage')
    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    description = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class SubImage(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField()

    def __str__(self):
        return "Изображение для {} ({})".format(self.content_object.title, self.content_object.category.name)


class Ball(Product):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True,
                                 default=Category.objects.get(slug='balls').pk, editable=False)
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.SET_NULL, null=True,
                                    blank=True)
    diameter = models.CharField(max_length=255, verbose_name='Диаметр')
    material = models.CharField(max_length=255, verbose_name='Материал камеры')
    weight = models.CharField(max_length=255, verbose_name='Вес')

    def __str__(self):
        return "{}: {}".format(self.subcategory.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product')


class TennisTable(Product):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True,
                                 default=Category.objects.get(slug='tennis_tables').pk, editable=False)
    material = models.CharField(max_length=255, verbose_name='Материал столешницы')
    size = models.CharField(max_length=255, verbose_name='Размеры упаковки')
    weight = models.CharField(max_length=255, verbose_name='Вес')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product')


class Treadmill(Product):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True,
                                 default=Category.objects.get(slug='treadmills').pk, editable=False)
    max_weight = models.CharField(max_length=255, verbose_name='Максимальный вес пользователя')
    max_speed = models.CharField(max_length=255, verbose_name='Максимальная скорость')
    engine_power = models.CharField(max_length=255, verbose_name='Мощность двигателя')
    weight = models.CharField(max_length=255, verbose_name='Вес')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product')


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Cart(models.Model):

    owner = models.ForeignKey(Customer, verbose_name='Владелец корзины', blank=True, null=True,
                              on_delete=models.CASCADE)
    total_products = models.PositiveIntegerField(default=0, verbose_name='Общее количество')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Сумма')
    for_anonymous_user = models.BooleanField(verbose_name='Анонимный пользователь', default=False)

    def __str__(self):
        return "Корзина {} ({})".format(self.id, self.owner.user.username)

    def save(self, *args, **kwargs):
        cart_data = CartProduct.objects.filter(cart_id=self.id).aggregate(models.Sum('total_price'), models.Sum('qty'))
        if cart_data.get('qty__sum'):
            self.total_products = cart_data.get('qty__sum')
            if cart_data.get('total_price__sum'):
                self.total_price = cart_data.get('total_price__sum')
            else:
                self.total_price = 0
        else:
            self.total_products = 0
        super().save(*args, **kwargs)


class CartProduct(models.Model):

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Сумма')

    def __str__(self):
        return "Продукт для корзины {}: {}".format(self.cart.id, self.content_object.title)

    def save(self, *args, **kwargs):
        self.total_price = self.qty * self.content_object.price
        if self.qty == 0:
            super().delete(*args, **kwargs)
        else:
            super().save(*args, **kwargs)