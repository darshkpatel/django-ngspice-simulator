# Generated by Django 3.0.2 on 2020-02-03 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='FilesUploader',
        ),
    ]