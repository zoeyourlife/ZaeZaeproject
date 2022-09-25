# Generated by Django 4.0.6 on 2022-09-25 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1, '글을 작성해주세요.')]),
        ),
    ]
