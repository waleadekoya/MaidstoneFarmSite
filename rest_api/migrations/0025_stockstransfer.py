# Generated by Django 4.0 on 2022-03-17 05:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0024_pen_responsible'),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTimeRecorded', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('Snail', 'Snail'), ('Egg', 'Egg')], max_length=100, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('comments', models.TextField(null=True)),
                ('destinationPen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.pen')),
                ('sourcePen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_pen', to='rest_api.pen')),
            ],
            options={
                'verbose_name_plural': 'Stocks Transfers',
                'db_table': 'stocks_transfers',
                'managed': True,
            },
        ),
    ]
