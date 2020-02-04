# Generated by Django 3.0.2 on 2020-02-03 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0002_auto_20200203_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='spiceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('size', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_time', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='FilesUploader',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_app.User'),
        ),
        migrations.AddField(
            model_name='spicefile',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_app.Task'),
        ),
    ]