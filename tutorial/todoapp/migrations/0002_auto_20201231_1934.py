# Generated by Django 3.1.4 on 2021-01-01 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user_created',
        ),
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
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Critically important'), (2, 'Very important'), (3, 'Highly important'), (4, 'Medium important'), (5, 'Low important')], default=5),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='remind_me_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
