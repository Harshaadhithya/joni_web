# Generated by Django 4.0.6 on 2022-07-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
                ('main_image', models.ImageField(upload_to='service_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=60)),
                ('client_organisation', models.CharField(max_length=30)),
                ('client_position', models.CharField(max_length=30)),
                ('client_review', models.CharField(max_length=500)),
                ('client_profile_img', models.ImageField(upload_to='client_profile_img/')),
            ],
        ),
    ]
