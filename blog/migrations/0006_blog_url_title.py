# Generated by Django 3.2.15 on 2022-08-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url_title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]