# Generated by Django 3.2.16 on 2024-06-11 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20240611_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='following',
        ),
    ]
