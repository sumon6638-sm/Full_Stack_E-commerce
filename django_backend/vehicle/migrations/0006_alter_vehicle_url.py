# Generated by Django 4.0.4 on 2022-05-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_remove_vehicle_fashion_vehicle_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='url',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
