# Generated by Django 3.2.4 on 2021-09-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210924_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]