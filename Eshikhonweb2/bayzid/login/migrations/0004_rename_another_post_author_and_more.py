# Generated by Django 5.1.4 on 2024-12-23 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='another',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='user_info',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user_info',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user_info',
            old_name='last_name',
            new_name='lname',
        ),
    ]
