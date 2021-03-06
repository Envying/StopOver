# Generated by Django 2.2 on 2019-05-13 03:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190511_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='car_license_name',
            field=models.CharField(default='Full Name', max_length=75, validators=[django.core.validators.RegexValidator(code='invalid_license_name', message='Full name is incorrect', regex='^[a-zA-Z\\s]+$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='car_license_type',
            field=models.IntegerField(choices=[(1, 'Full'), (2, 'Green Provisional'), (3, 'Red Provisional'), (4, 'Learner')], default=1),
        ),
        migrations.AlterField(
            model_name='account',
            name='car_license',
            field=models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(code='invalid_license', message='Postcode is incorrect', regex='^[0-9]{7}$')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Mobile Number is incorrect', regex='^[0-9]{10}$')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='postcode',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_postcode', message='Postcode is incorrect', regex='^[0-9]{4}$')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='street_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_street_name', message='Street name is incorrect', regex='(^[a-zA-Z]+$)|(^[a-zA-Z]+\\s[a-zA-Z]+$)')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='street_number',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_street_number', message='Street Number is incorrect', regex='^[0-9]+[a-z]*$')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='suburb',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='invalid_suburb', message='Suburb is incorrect', regex='(^[a-zA-Z]+$)|(^[a-zA-Z]+\\s[a-zA-Z]+$)')]),
        ),
    ]
