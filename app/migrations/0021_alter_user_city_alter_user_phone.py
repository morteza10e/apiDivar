# Generated by Django 5.1.2 on 2024-11-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_user_city_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
