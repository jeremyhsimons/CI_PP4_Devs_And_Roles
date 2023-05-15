# Generated by Django 3.2.19 on 2023-05-15 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('linkedin', models.CharField(max_length=200)),
                ('github_username', models.CharField(max_length=200)),
                ('why_company', models.TextField(max_length=2000)),
                ('why_role', models.TextField(max_length=2000)),
                ('why_you', models.TextField(max_length=2000)),
                ('supporting_docs', models.FileField(blank=True, upload_to='')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application', to=settings.AUTH_USER_MODEL)),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application', to='job_board.jobposting')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]