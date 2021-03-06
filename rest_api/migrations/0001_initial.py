# Generated by Django 4.0 on 2021-12-22 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pen',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('size', models.CharField(choices=[('3 x 6 feet', '3 x 6 feet'), ('5 x 6 feet', '5 x 6 feet')], max_length=100)),
            ],
            options={
                'db_table': 'pen_numbers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SnailsCurrentInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(choices=[('AMO', 'AMO'), ('AMS', 'AMS')], max_length=100, null=True)),
                ('dateRecorded', models.DateField()),
                ('totalCount', models.IntegerField()),
                ('penNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.pen')),
            ],
            options={
                'db_table': 'snails_current_totals',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SnailsActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(choices=[('AMO', 'AMO'), ('AMS', 'AMS')], max_length=100, null=True)),
                ('dateRecorded', models.DateField()),
                ('totalMortalities', models.IntegerField()),
                ('newBreederStocks', models.IntegerField()),
                ('newEggsCollected', models.IntegerField()),
                ('newBabySnails', models.IntegerField()),
                ('hatchedEggsCount', models.IntegerField()),
                ('damagedEggsCount', models.IntegerField()),
                ('snailReshuffle', models.IntegerField()),
                ('penNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.pen')),
            ],
            options={
                'db_table': 'snails_activities',
                'managed': True,
            },
        ),
    ]
