# Generated by Django 3.1.1 on 2020-09-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasklable',
            old_name='lable_id',
            new_name='lable',
        ),
        migrations.RenameField(
            model_name='tasklable',
            old_name='task_id',
            new_name='task',
        ),
    ]