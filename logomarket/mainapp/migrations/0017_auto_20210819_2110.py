# Generated by Django 3.2.5 on 2021-08-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20210816_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Сумма'),
        ),
    ]