# Generated by Django 4.2.4 on 2023-08-04 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='slug',
            new_name='uuid',
        ),
    ]
