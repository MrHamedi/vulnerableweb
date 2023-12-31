# Generated by Django 4.2.4 on 2023-08-04 18:52

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='موضوع')),
                ('text', ckeditor.fields.RichTextField(verbose_name='متن')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')),
            ],
            options={
                'verbose_name': 'مبحث',
                'verbose_name_plural': 'مباحث',
                'ordering': ('created', 'updated'),
            },
        ),
    ]
