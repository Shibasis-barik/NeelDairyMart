# Generated by Django 5.1.2 on 2024-10-23 09:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_category_customeer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PN', 'Paneer'), ('ML', 'Milk'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('IC', 'Ice-cream'), ('MS', 'Milkshake')], max_length=2),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('ML', 'Meghalaya'), ('LD', 'Lakshadweep'), ('LA', 'Ladakh'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('CH', 'Chandigarh'), ('TN', 'Tamil Nadu'), ('BR', 'Bihar'), ('HR', 'Haryana'), ('GA', 'Goa'), ('AN', 'Andaman and Nicobar Islands'), ('OR', 'Odisha'), ('DL', 'Delhi'), ('MH', 'Maharashtra'), ('JH', 'Jharkhand'), ('AP', 'Andhra Pradesh'), ('KA', 'Karnataka'), ('GJ', 'Gujarat'), ('UP', 'Uttar Pradesh'), ('MN', 'Manipur'), ('MP', 'Madhya Pradesh'), ('TR', 'Tripura'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('JK', 'Jammu and Kashmir'), ('AR', 'Arunachal Pradesh'), ('CT', 'Chhattisgarh'), ('HP', 'Himachal Pradesh'), ('UK', 'Uttarakhand'), ('PY', 'Puducherry'), ('WB', 'West Bengal'), ('AS', 'Assam'), ('SK', 'Sikkim'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'), ('KL', 'Kerala'), ('TS', 'Telangana')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Customeer',
        ),
    ]
