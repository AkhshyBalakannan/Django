# Generated by Django 3.2.5 on 2021-07-16 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210716_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='CODE',
            new_name='code',
        ),
    ]