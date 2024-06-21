# Generated by Django 4.2.5 on 2023-11-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0022_alter_weblogvideocomment_blog'),
        ('product_app', '0010_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likee',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_products', to='weblog_app.ipmodel'),
        ),
    ]