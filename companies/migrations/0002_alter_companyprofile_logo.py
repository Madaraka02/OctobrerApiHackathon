# Generated by Django 4.1.2 on 2022-10-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='companies/images'),
        ),
    ]
