# Generated by Django 4.0 on 2022-03-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0025_stockstransfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='snailsactivity',
            name='feedConsumptionRate',
            field=models.FloatField(default=0, null=True),
        ),
    ]