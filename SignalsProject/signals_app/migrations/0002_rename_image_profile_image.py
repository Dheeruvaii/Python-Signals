# Generated by Django 4.0 on 2024-02-14 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signals_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Image',
            new_name='image',
        ),
    ]
