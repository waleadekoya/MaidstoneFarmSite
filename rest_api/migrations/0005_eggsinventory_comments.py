# Generated by Django 4.0 on 2021-12-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_eggsinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggsinventory',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]