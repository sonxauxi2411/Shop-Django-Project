# Generated by Django 4.2 on 2023-04-26 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_a', '0007_cartitem_delete_carts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total',
        ),
    ]
