# Generated by Django 5.1.2 on 2024-10-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_product_image_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LS', 'Lassi'), ('GH', 'Ghee'), ('IC', 'Ice-cream'), ('MS', 'Milkshake'), ('ML', 'Milk'), ('PN', 'Paneer'), ('CZ', 'Cheese'), ('CR', 'Curd')], max_length=2),
        ),
    ]
