# Generated by Django 5.0.6 on 2024-07-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_player_district_alter_player_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='relation',
            field=models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Guardian', 'Guardian'), ('Other', 'Other')], max_length=20, null=True),
        ),
    ]
