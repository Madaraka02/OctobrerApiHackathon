# Generated by Django 4.1.2 on 2022-10-07 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_companyprofile_logo'),
        ('advocates', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advocates', to='companies.companyprofile'),
        ),
    ]
