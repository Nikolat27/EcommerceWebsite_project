# Generated by Django 4.2.5 on 2023-11-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0020_weblogcomment_study_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogcomment',
            name='study_time',
        ),
        migrations.AddField(
            model_name='weblogvideo',
            name='study_time',
            field=models.IntegerField(default=5),
        ),
    ]
