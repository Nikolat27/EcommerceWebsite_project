# Generated by Django 4.2.5 on 2023-11-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0003_alter_orderitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
