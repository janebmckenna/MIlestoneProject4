# Generated by Django 3.2.25 on 2024-04-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20240413_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='period',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='player_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='team_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
