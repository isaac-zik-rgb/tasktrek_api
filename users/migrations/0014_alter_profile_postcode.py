# Generated by Django 4.2.5 on 2023-11-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profile_additional_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='postcode',
            field=models.IntegerField(null=True),
        ),
    ]
