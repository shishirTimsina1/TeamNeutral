# Generated by Django 3.2.9 on 2021-11-30 11:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_events_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[django.core.validators.MinValueValidator(datetime.date.today)]),
        ),
    ]