# Generated by Django 3.0.7 on 2020-11-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality_rating',
            name='ticket_id',
            field=models.IntegerField(unique=True),
        ),
    ]
