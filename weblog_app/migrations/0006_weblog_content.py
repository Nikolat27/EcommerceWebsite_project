# Generated by Django 4.2.5 on 2023-11-05 20:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0005_alter_weblog_main_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
