# Generated by Django 4.2.5 on 2023-10-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
