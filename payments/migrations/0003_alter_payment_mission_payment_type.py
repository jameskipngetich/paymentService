# Generated by Django 5.2.1 on 2025-06-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_is_alo_member_member_is_alo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='mission_payment_type',
            field=models.CharField(blank=True, choices=[('20_BOB', '20 Bob Challenge'), ('50_BOB', '50 Bob Challenge'), ('COHORT', 'Cohort Payment'), ('FAMILY', 'Family Payment'), ('MINI_FUNDRAISER', 'Mini Fundraiser '), ('MUSIC_CONCERT', 'music concert'), ('MEGA_FUNDRAISER', 'Mega Fundraiser')], max_length=20, null=True),
        ),
    ]
