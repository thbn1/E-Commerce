# Generated by Django 5.0.3 on 2024-07-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0044_alter_product_productrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productrating',
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
    ]
