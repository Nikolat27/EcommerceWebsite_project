# Generated by Django 4.2.5 on 2023-10-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_forgotenpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgotenpassword',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]