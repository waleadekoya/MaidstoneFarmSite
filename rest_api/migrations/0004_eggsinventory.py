# Generated by Django 4.0 on 2021-12-23 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_alter_snailsactivity_damagedeggscount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EggsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRecorded', models.DateField()),
                ('totalCount', models.IntegerField(default=0)),
                ('penNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.pen')),
            ],
            options={
                'db_table': 'eggs_table',
                'managed': True,
            },
        ),
    ]
