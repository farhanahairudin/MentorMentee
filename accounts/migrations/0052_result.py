# Generated by Django 3.0.7 on 2021-01-02 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_auto_20210103_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('grade', models.CharField(max_length=200, null=True)),
                ('types', models.CharField(choices=[('Quiz', 'Quiz'), ('Mid-Exam', 'Mid-Exam'), ('Final-Exam', 'Final-Exam')], max_length=200, null=True)),
                ('mentee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Mentee')),
            ],
        ),
    ]
