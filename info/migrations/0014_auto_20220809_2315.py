# Generated by Django 3.2.15 on 2022-08-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_enquiry_enquired_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enquired_for',
            field=models.CharField(blank=True, choices=[('App Development', 'App Development'), ('Web Development', 'Web Development'), ('Search Engine Optimization', 'Search Engine Optimization'), ('Search Engine Marketing', 'Search Engine Marketing'), ('App Store Optimization', 'App Store Optimization'), ('Social Media Marketing', 'Social Media Marketing'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='client_organisation',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='client_review',
            field=models.CharField(max_length=1000),
        ),
    ]
