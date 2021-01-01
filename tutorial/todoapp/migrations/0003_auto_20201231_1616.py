# Generated by Django 3.1.4 on 2020-12-31 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20201231_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='due_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
