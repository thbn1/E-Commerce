# Generated by Django 4.1.1 on 2023-08-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_product_webapp_prod_product_e3fe25_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product',
            name='webapp_prod_product_e3fe25_idx',
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-productname'], name='webapp_prod_product_8c50f0_idx'),
        ),
    ]
