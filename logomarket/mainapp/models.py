from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__.meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class MaxImageSizeError(Exception):
    pass


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


class Product(models.Model):

    MAX_IMAGE_SIZE = 524288

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        image = self.image
        if image.size > self.MAX_IMAGE_SIZE:
            raise MaxImageSizeError('Загруженное изображение имеет слишком большой объем')
        super().save(*args, **kwargs)


class Treadmill(Product):

    weight = models.CharField(max_length=255, verbose_name='Вес дорожки')
    max_weight = models.CharField(max_length=255, verbose_name='Максимальный вес пользователя')
    max_speed = models.CharField(max_length=255, verbose_name='Максимальная скорость')
    engine_power = models.CharField(max_length=255, verbose_name='Мощность двигателя')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)

    def get_absolte_url(self):
        return get_product_url(self, 'product_detail')


class Ball(Product):
    weight = models.CharField(max_length=255, verbose_name='Вес мяча')
    diameter = models.CharField(max_length=255, verbose_name='Диаметр')
    material = models.CharField(max_length=255, verbose_name='Материал камеры')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)

    def get_absolte_url(self):
        return get_product_url(self, 'product_detail')


class TennisTable(Product):

    weight = models.CharField(max_length=255, verbose_name='Вес стола')
    material = models.CharField(max_length=255, verbose_name='Материал столешницы')
    size = models.CharField(max_length=255, verbose_name='Размеры')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)

    def get_absolte_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец корзины', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)