# Generated by Django 4.0 on 2021-12-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0016_alter_closingsnailsinventory_datetimerecorded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snailsactivity',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
