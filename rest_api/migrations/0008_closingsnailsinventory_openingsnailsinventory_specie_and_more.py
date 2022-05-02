# Generated by Django 4.0 on 2021-12-23 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_remove_snailsactivity_hatchedeggscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosingSnailsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRecorded', models.DateField()),
                ('totalCount', models.IntegerField(default=0)),
                ('penNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.pen')),
            ],
            options={
                'db_table': 'closing_snails_inventory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OpeningSnailsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCount', models.IntegerField(default=0)),
                ('dateRecorded', models.DateField()),
                ('penNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.pen')),
            ],
            options={
                'db_table': 'opening_snails_inventory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(choices=[('AMO', 'AMO'), ('AMS', 'AMS')], max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'snails_species',
                'managed': True,
            },
        ),
        migrations.AlterModelTable(
            name='eggsinventory',
            table='eggs_inventory',
        ),
        migrations.DeleteModel(
            name='SnailsCurrentInventory',
        ),
        migrations.AddField(
            model_name='closingsnailsinventory',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.specie', to_field='specie'),
        ),
        migrations.AlterField(
            model_name='snailsactivity',
            name='species',
            field=models.ForeignKey(default='AMO', on_delete=django.db.models.deletion.CASCADE, to='rest_api.specie', to_field='specie'),
        ),
    ]