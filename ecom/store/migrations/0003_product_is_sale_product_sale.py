# Generated by Django 5.1.2 on 2024-10-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
