# Generated by Django 3.2.4 on 2021-08-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0003_alter_exchange_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='recieve_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, verbose_name='recieve amount'),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='send_amount',
            field=models.DecimalField(decimal_places=4, max_digits=15, verbose_name='send amount'),
        ),
    ]
