# Generated by Django 3.2.7 on 2021-09-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_alter_coupon_customer_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='customer_cpf',
            field=models.CharField(help_text='Somente números', max_length=11, verbose_name='CPF do cliente'),
        ),
    ]