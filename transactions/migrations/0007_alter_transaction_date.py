# Generated by Django 4.2.7 on 2023-11-27 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_remove_transaction_user_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 27, 15, 35, 2, 528097)),
        ),
    ]