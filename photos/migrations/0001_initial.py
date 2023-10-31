# Generated by Django 4.2.1 on 2023-10-31 11:52

from django.db import migrations, models
import django.db.models.deletion
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_taken', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=photos.models.path_file_name)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_uploaded', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='photos.category')),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='photos.session')),
            ],
        ),
    ]
