# Generated by Django 3.2.4 on 2021-06-14 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210614_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]