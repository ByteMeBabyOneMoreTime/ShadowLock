# Generated by Django 5.1.5 on 2025-02-02 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShadowLock', '0002_passwords_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwords',
            name='created_by',
        ),
    ]
