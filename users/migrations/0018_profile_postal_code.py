# Generated by Django 4.2.5 on 2023-11-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_profile_postal_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
