# Generated by Django 3.1.1 on 2020-10-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shippingdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order'),
        ),
    ]
