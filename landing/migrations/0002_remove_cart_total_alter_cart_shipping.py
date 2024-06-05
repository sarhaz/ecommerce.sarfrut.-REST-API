# Generated by Django 5.0.6 on 2024-05-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.AlterField(
            model_name='cart',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]