# Generated by Django 3.2 on 2021-06-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='writer',
        ),
    ]
