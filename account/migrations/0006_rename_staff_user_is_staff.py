# Generated by Django 4.0.4 on 2022-07-07 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='staff',
            new_name='is_staff',
        ),
    ]
