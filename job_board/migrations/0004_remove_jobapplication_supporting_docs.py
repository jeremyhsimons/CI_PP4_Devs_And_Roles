# Generated by Django 3.2.19 on 2023-06-06 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0003_alter_jobapplication_supporting_docs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='supporting_docs',
        ),
    ]
