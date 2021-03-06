# Generated by Django 2.1.2 on 2018-12-13 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20181210_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_description',
            field=models.TextField(help_text='Enter Brand Description', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='brand_images/%Y/%m/%d/'),
        ),
    ]
