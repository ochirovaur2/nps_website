# Generated by Django 3.0.7 on 2020-12-11 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201130_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality_rating',
            name='ticket_id',
            field=models.IntegerField(),
        ),
    ]
