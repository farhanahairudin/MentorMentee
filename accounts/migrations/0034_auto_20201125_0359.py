# Generated by Django 3.0.7 on 2020-11-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_session_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.TextField(default='Pending', null=True, verbose_name='Status'),
        ),
    ]