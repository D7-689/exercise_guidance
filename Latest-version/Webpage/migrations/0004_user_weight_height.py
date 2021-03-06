# Generated by Django 3.2.8 on 2022-04-15 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Webpage', '0003_learner'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Weight_Height',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.BigIntegerField(max_length=250, null=True)),
                ('weight', models.BigIntegerField(max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
