# Generated by Django 4.2.5 on 2023-10-04 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotenPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
