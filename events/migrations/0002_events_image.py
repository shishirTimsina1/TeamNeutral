# Generated by Django 3.2.9 on 2021-11-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events-images/'),
        ),
    ]