# Generated by Django 4.0 on 2021-12-29 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0019_alter_closingsnailsinventory_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClosingSnailsInventory',
            new_name='SnailsInventory',
        ),
    ]
