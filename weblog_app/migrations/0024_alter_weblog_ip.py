# Generated by Django 5.0.6 on 2024-06-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weblog_app", "0023_remove_weblogvideo_main_picture_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weblog",
            name="ip",
            field=models.ManyToManyField(
                related_name="post_views", to="weblog_app.ipmodel"
            ),
        ),
    ]
