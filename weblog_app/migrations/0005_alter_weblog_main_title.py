# Generated by Django 4.2.5 on 2023-11-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0004_weblog_main_image_weblog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='main_title',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
