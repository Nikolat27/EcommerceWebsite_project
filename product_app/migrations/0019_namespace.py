# Generated by Django 4.2.5 on 2023-11-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0018_productdetail_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
    ]