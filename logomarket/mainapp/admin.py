from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.db.models import Q
from django.contrib import admin
from .models import *


class BallAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcategory':
            return ModelChoiceField(SubCategory.objects.filter(category_id=Category.objects.get(slug='balls')))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ContentTypeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'content_type':
            return ModelChoiceField(
                ContentType.objects.filter(Q(model='ball') | Q(model='treadmill') | Q(model='tennistable')))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SubImageAdmin(ContentTypeAdmin):
    pass


class CartProductAdmin(ContentTypeAdmin):
    pass


admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(SubImage, SubImageAdmin)
admin.site.register(Treadmill)
admin.site.register(Ball, BallAdmin)
admin.site.register(TennisTable)

admin.site.register(CartProduct, CartProductAdmin)

admin.site.register(Cart)

admin.site.register(Customer)
