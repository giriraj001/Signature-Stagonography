# Generated by Django 4.0.1 on 2022-05-29 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='image',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]