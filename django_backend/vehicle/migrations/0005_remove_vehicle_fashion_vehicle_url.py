# Generated by Django 4.0.4 on 2022-05-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_remove_category_fashion_vehicle_fashion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='fashion',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
