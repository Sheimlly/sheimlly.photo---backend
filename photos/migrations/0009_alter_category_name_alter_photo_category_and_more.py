# Generated by Django 4.2.1 on 2023-10-31 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_alter_photo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='photos.category'),
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
