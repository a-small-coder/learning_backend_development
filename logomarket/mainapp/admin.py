from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from .models import *


class BallAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcategory':
            return ModelChoiceField(SubCategory.objects.filter(category_id=Category.objects.get(slug='balls')))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(Treadmill)
admin.site.register(Ball, BallAdmin)
admin.site.register(TennisTable)

admin.site.register(CartProduct)

admin.site.register(Cart)

admin.site.register(Customer)
