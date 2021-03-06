# Generated by Django 3.2.8 on 2022-04-17 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0008_alter_user_weight_height_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_weight_height',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='user_weight_height',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True),
        ),
    ]
