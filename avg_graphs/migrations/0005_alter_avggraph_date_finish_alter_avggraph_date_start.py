# Generated by Django 4.2.7 on 2023-11-27 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avg_graphs', '0004_alter_avggraph_date_finish_alter_avggraph_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avggraph',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2023, 11, 27, 3, 36, 12, 93679)),
        ),
        migrations.AlterField(
            model_name='avggraph',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2023, 11, 27, 3, 36, 12, 93679)),
        ),
    ]