# Generated by Django 4.2.4 on 2023-08-26 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ('-created_date',)},
        ),
    ]
