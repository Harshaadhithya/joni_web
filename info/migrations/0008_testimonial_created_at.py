# Generated by Django 4.0.6 on 2022-07-25 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_service_short_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
