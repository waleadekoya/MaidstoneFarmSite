# Generated by Django 4.0 on 2022-02-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0020_rename_closingsnailsinventory_snailsinventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eggsinventory',
            options={'managed': True, 'verbose_name_plural': 'Eggs Inventory'},
        ),
        migrations.AlterModelOptions(
            name='pen',
            options={'managed': True, 'verbose_name_plural': 'Snails Pen Structure'},
        ),
        migrations.AlterModelOptions(
            name='snailsactivity',
            options={'managed': True, 'verbose_name_plural': 'Snails Activities'},
        ),
        migrations.AlterModelOptions(
            name='snailsinventory',
            options={'managed': True, 'verbose_name_plural': 'Snails Inventory'},
        ),
        migrations.AlterModelOptions(
            name='specie',
            options={'managed': True, 'verbose_name_plural': 'Snails Species'},
        ),
        migrations.AddField(
            model_name='pen',
            name='responsible',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
