# Generated by Django 3.2.5 on 2021-07-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_weight',
            field=models.IntegerField(default=50),
        ),
    ]
