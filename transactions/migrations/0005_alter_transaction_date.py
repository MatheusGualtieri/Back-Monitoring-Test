# Generated by Django 4.2.7 on 2023-11-27 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 26, 21, 55, 47, 867255)),
        ),
    ]
