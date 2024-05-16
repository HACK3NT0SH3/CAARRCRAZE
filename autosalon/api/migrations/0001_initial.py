# Generated by Django 4.2.5 on 2024-05-11 23:04

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
            name='Car',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Brand', models.CharField(blank=True, max_length=50, null=True)),
                ('Model', models.CharField(blank=True, max_length=50, null=True)),
                ('Year', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, default=0, null=True)),
                ('Description', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images/')),
                ('Trade_in', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('DateTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('totalPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('mileage', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradeIn',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userCar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usercar')),
            ],
        ),
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.car')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.car')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.order')),
            ],
        ),
    ]