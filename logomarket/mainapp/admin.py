from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class TreadmillAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:12px;">Объем файла не должен превышать 0.5MB'.format(
                Product.MAX_IMAGE_SIZE
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Загруженное изображение имеет слишком большой объем')
        return image


class TreadmillAdmin(admin.ModelAdmin):

    form = TreadmillAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='treadmills'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BallAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='balls'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TennisTableAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tennis_tables'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Treadmill, TreadmillAdmin)
admin.site.register(Ball, BallAdmin)
admin.site.register(TennisTable, TennisTableAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
