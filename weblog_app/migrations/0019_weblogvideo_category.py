# Generated by Django 4.2.5 on 2023-11-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0018_weblogvideocomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblogvideo',
            name='category',
            field=models.ManyToManyField(related_name='video_categories', to='weblog_app.weblogcategroy'),
        ),
    ]
