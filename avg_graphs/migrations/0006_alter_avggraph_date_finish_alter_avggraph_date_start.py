# Generated by Django 4.2.7 on 2023-11-27 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avg_graphs', '0005_alter_avggraph_date_finish_alter_avggraph_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avggraph',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2023, 11, 27, 15, 35, 2, 531087)),
        ),
        migrations.AlterField(
            model_name='avggraph',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2023, 11, 27, 15, 35, 2, 531087)),
        ),
    ]
