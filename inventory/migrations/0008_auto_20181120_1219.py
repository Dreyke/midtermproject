# Generated by Django 2.1.2 on 2018-11-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_product_custom_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='custom_field',
            field=models.CharField(max_length=100, null=True),
        ),
    ]