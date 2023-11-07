# Generated by Django 4.2.5 on 2023-11-07 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Address_Line1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='Address_Line2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='postcode',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='working_experience',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='years_of_experience',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
