# Generated by Django 4.2.4 on 2023-08-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='fee_type',
            field=models.CharField(max_length=20),
        ),
    ]
