# Generated by Django 2.1.2 on 2018-11-30 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20181120_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product-images'),
        ),
    ]