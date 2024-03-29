# Generated by Django 4.0 on 2024-03-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals_app', '0002_rename_image_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Mango', 'Mango'), ('Apple', 'Apple'), ('Orange', 'Orange'), ('Banana', 'Banana')], max_length=30)),
                ('quantity', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_item', models.CharField(choices=[('Mango', 'Mango'), ('Apple', 'Apple'), ('Orange', 'Orange'), ('Banana', 'Banana')], max_length=10)),
                ('available_quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
