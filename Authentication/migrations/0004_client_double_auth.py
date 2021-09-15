# Generated by Django 3.2.4 on 2021-09-02 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_client_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='double_auth',
            field=models.BooleanField(default=False, help_text='Designed whether if client has double authentication or not', verbose_name='double authentication'),
        ),
    ]