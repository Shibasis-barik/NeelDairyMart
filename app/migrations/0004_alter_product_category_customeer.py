# Generated by Django 5.1.2 on 2024-10-23 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('PN', 'Paneer'), ('IC', 'Ice-cream'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('LS', 'Lassi')], max_length=2),
        ),
        migrations.CreateModel(
            name='Customeer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('MN', 'Manipur'), ('TS', 'Telangana'), ('GJ', 'Gujarat'), ('LA', 'Ladakh'), ('MP', 'Madhya Pradesh'), ('WB', 'West Bengal'), ('AS', 'Assam'), ('MH', 'Maharashtra'), ('AR', 'Arunachal Pradesh'), ('AP', 'Andhra Pradesh'), ('JH', 'Jharkhand'), ('TN', 'Tamil Nadu'), ('OR', 'Odisha'), ('JK', 'Jammu and Kashmir'), ('TR', 'Tripura'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('RJ', 'Rajasthan'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('CT', 'Chhattisgarh'), ('BR', 'Bihar'), ('HP', 'Himachal Pradesh'), ('DL', 'Delhi'), ('GA', 'Goa'), ('HR', 'Haryana'), ('UK', 'Uttarakhand'), ('LD', 'Lakshadweep'), ('UP', 'Uttar Pradesh'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'), ('CH', 'Chandigarh'), ('PY', 'Puducherry'), ('AN', 'Andaman and Nicobar Islands'), ('NL', 'Nagaland'), ('PB', 'Punjab'), ('SK', 'Sikkim')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
