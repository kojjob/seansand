# Generated by Django 3.1 on 2021-02-04 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0002_auto_20210203_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='baths',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='beddrooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_in',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_out',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='city',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='guests',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='instant_book',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]