# Generated by Django 3.2.19 on 2023-05-16 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_message', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]
