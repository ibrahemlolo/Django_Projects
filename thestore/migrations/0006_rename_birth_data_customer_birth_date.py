# Generated by Django 5.0 on 2023-12-16 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thestore', '0005_customer_membershib'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birth_data',
            new_name='birth_date',
        ),
    ]
