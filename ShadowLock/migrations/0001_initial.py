# Generated by Django 5.1.5 on 2025-02-02 19:34

import encrypted_model_fields.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=5000)),
                ('environment', encrypted_model_fields.fields.EncryptedTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shared_with', models.ManyToManyField(related_name='Environment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Saved Environment',
            },
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=5000)),
                ('password', encrypted_model_fields.fields.EncryptedTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shared_with', models.ManyToManyField(related_name='Passwords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Saved Password',
            },
        ),
    ]
