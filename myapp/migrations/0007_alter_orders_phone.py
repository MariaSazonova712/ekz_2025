# Generated by Django 4.2.7 on 2024-11-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
    ]