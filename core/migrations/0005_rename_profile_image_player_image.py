# Generated by Django 5.0.6 on 2024-07-02 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_image_player_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='profile_image',
            new_name='image',
        ),
    ]
