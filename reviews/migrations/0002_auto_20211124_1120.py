# Generated by Django 3.2.9 on 2021-11-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
