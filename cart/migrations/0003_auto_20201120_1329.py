# Generated by Django 3.1.3 on 2020-11-20 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20201120_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='limit_period',
            field=models.DateTimeField(null=True),
        ),
    ]