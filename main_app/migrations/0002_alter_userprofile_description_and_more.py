# Generated by Django 5.0.2 on 2024-02-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='discord1_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='discord1_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='discord2_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='discord2_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram1_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram1_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram2_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram2_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin1_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin1_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin2_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin2_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='x1_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='x1_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='x2_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='x2_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='youtube1_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='youtube1_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='youtube2_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='youtube2_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
