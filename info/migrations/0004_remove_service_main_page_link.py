# Generated by Django 4.0.6 on 2022-07-24 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_service_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='main_page_link',
        ),
    ]
