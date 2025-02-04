# Generated by Django 5.0.6 on 2024-07-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_player_address_player_district_player_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='district',
            field=models.CharField(blank=True, choices=[('KA', [('Bangalore', 'Bangalore'), ('Mysore', 'Mysore'), ('Hubli', 'Hubli')]), ('MH', [('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Nagpur', 'Nagpur')]), ('TN', [('Chennai', 'Chennai'), ('Coimbatore', 'Coimbatore'), ('Madurai', 'Madurai')])], max_length=100, null=True),
        ),
    ]
