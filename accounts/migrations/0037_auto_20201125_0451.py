# Generated by Django 3.0.7 on 2020-11-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_session_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
