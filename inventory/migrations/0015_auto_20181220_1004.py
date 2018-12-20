# Generated by Django 2.1.2 on 2018-12-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20181218_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('y', 'In Stock'), ('n', 'Out of Stock')], default='y', help_text='Product Availability', max_length=1),
        ),
    ]
