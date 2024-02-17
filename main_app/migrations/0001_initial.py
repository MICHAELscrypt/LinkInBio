# Generated by Django 5.0.2 on 2024-02-17 20:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1024)),
                ('instagram1_text', models.CharField(max_length=1024)),
                ('instagram1_link', models.CharField(max_length=1024)),
                ('instagram2_text', models.CharField(max_length=1024)),
                ('instagram2_link', models.CharField(max_length=1024)),
                ('x1_text', models.CharField(max_length=1024)),
                ('x1_link', models.CharField(max_length=1024)),
                ('x2_text', models.CharField(max_length=1024)),
                ('x2_link', models.CharField(max_length=1024)),
                ('linkedin1_text', models.CharField(max_length=1024)),
                ('linkedin1_link', models.CharField(max_length=1024)),
                ('linkedin2_text', models.CharField(max_length=1024)),
                ('linkedin2_link', models.CharField(max_length=1024)),
                ('discord1_text', models.CharField(max_length=1024)),
                ('discord1_link', models.CharField(max_length=1024)),
                ('discord2_text', models.CharField(max_length=1024)),
                ('discord2_link', models.CharField(max_length=1024)),
                ('youtube1_text', models.CharField(max_length=1024)),
                ('youtube1_link', models.CharField(max_length=1024)),
                ('youtube2_text', models.CharField(max_length=1024)),
                ('youtube2_link', models.CharField(max_length=1024)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]