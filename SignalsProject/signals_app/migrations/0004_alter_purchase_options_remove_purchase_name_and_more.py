# Generated by Django 4.0 on 2024-03-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals_app', '0003_purchase_stock_delete_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Purchase', 'verbose_name_plural': 'Purchases'},
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='name',
        ),
        migrations.AddField(
            model_name='purchase',
            name='item',
            field=models.CharField(choices=[('Banana', 'Banana'), ('Mango', 'Mango'), ('Orange', 'Orange'), ('Apple', 'Apple')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='available_item',
            field=models.CharField(choices=[('Banana', 'Banana'), ('Mango', 'Mango'), ('Orange', 'Orange'), ('Apple', 'Apple')], max_length=10),
        ),
    ]
