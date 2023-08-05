# Generated by Django 4.2.4 on 2023-08-05 19:20

from django.db import migrations, models
import topics.models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_rename_slug_topic_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='pic',
            field=models.ImageField(null=True, upload_to=topics.models.topic_image_upload_path, verbose_name='تصویر'),
        ),
    ]
