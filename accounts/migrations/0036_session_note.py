# Generated by Django 3.0.7 on 2020-11-24 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20201125_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='note',
            field=models.CharField(default='State your reason if you reject..', max_length=1000, null=True),
        ),
    ]