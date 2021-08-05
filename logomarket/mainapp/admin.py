from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from .models import *


class TreadmillAdmin(admin.ModelAdmin):

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
admin.site.register(SubCategory)

admin.site.register(Treadmill, TreadmillAdmin)
admin.site.register(Ball, BallAdmin)
admin.site.register(TennisTable, TennisTableAdmin)

admin.site.register(CartProduct)

admin.site.register(Cart)

admin.site.register(Customer)
