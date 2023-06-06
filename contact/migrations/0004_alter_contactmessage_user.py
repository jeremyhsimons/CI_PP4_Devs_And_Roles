# Generated by Django 3.2.19 on 2023-06-06 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0003_rename_body_contactmessage_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_message', to=settings.AUTH_USER_MODEL),
        ),
    ]
