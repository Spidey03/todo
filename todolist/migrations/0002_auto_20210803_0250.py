# Generated by Django 3.1.1 on 2021-08-03 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertask',
            name='editable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertask',
            name='stage',
            field=models.BooleanField(default=False),
        ),
    ]