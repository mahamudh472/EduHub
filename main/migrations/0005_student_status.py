# Generated by Django 4.2.4 on 2023-08-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_month_monthlyfee_onetimefee_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('running', 'Running'), ('finished', 'Finished')], default='N/A', max_length=15),
        ),
    ]