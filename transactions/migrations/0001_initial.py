# Generated by Django 4.2.7 on 2023-11-23 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('reversed', 'Reversed'), ('processing', 'Processing'), ('denied', 'Denied'), ('FAILED', 'Failed')], default='processing', max_length=50)),
                ('count', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
