# Generated by Django 2.1 on 2020-12-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_task_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_complete',
            field=models.IntegerField(default=0),
        ),
    ]