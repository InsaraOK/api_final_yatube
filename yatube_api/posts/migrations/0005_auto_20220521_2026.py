# Generated by Django 2.2.16 on 2022-05-21 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220521_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id',)},
        ),
    ]