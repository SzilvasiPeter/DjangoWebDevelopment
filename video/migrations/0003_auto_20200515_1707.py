# Generated by Django 3.0.6 on 2020-05-15 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20200515_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='release_dates',
            new_name='release_date',
        ),
    ]
