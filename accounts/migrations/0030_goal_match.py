# Generated by Django 3.0.7 on 2020-06-13 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20200613_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Match'),
        ),
    ]
