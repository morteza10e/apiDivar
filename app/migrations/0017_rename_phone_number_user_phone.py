# Generated by Django 5.1.2 on 2024-11-11 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_user_city_user_phone_number_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
