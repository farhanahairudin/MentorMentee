# Generated by Django 3.0.7 on 2021-01-02 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_auto_20210103_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='match',
        ),
        migrations.AddField(
            model_name='result',
            name='mentee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Mentee'),
        ),
    ]
