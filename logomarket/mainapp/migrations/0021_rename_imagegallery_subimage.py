# Generated by Django 3.2.5 on 2021-08-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mainapp', '0020_auto_20210821_2350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageGallery',
            new_name='SubImage',
        ),
    ]
