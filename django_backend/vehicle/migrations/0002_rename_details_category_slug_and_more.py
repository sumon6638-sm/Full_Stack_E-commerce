# Generated by Django 4.0.4 on 2022-04-29 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='details',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='details',
            new_name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='type',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='type',
        ),
    ]
