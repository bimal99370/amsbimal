# Generated by Django 5.0.6 on 2024-07-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_player_group_player_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, default='images/default_profile.jpg', null=True, upload_to='images/'),
        ),
    ]
