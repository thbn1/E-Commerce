# Generated by Django 4.1.1 on 2023-08-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_product_slug_alter_comment_pcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
