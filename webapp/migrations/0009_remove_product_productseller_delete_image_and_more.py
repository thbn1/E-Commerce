# Generated by Django 4.1.1 on 2023-07-27 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_product_productoldprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productseller',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
