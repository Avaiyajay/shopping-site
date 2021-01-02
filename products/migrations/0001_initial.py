# Generated by Django 3.1.1 on 2020-10-17 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('needshipping', models.BooleanField(blank=True, default=False)),
                ('dateoforder', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('shoes', 'Shoes'), ('watch', 'Watch'), ('tshirt', 'T-shirt'), ('jeans', 'Jeans')], max_length=6, null=True)),
                ('feachered', models.BooleanField(blank=True, null=True)),
                ('digital', models.BooleanField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-images')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120)),
                ('contactno', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('city', models.CharField(choices=[('surat', 'Surat'), ('ahmedabad', 'Ahmedabad'), ('vadodara', 'Vadodara')], max_length=9)),
                ('state', models.CharField(choices=[('gujarat', 'Gujarat'), ('mp', 'MP')], max_length=7)),
                ('zipcode', models.CharField(max_length=6)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
