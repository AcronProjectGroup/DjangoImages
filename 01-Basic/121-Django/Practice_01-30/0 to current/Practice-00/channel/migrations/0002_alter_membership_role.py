# Generated by Django 4.2.2 on 2023-07-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('normal', 'Normal'), ('vip', 'Vip')], default='normal', max_length=10),
        ),
    ]