# Generated by Django 4.2.5 on 2023-11-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0014_remove_productdetail_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='x',
            field=models.JSONField(blank=True, null=True),
        ),
    ]