# Generated by Django 3.2.5 on 2021-08-05 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ball',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subcategory', verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='SubCategoryBall',
        ),
    ]