# Generated by Django 4.0 on 2022-02-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0022_remove_pen_responsible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='TBC', max_length=100, unique=True)),
            ],
        ),
    ]
