# Generated by Django 3.2.9 on 2021-12-04 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0010_auto_20211202_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcomment',
            name='name',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='event_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
