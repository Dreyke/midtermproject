# Generated by Django 2.1.2 on 2018-11-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='product_images/%Y/%m/%d/'),
        ),
    ]
