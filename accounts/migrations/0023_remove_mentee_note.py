# Generated by Django 3.0.7 on 2020-06-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_remove_mentee_mentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='note',
        ),
    ]
