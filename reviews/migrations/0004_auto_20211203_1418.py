# Generated by Django 3.2.9 on 2021-12-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='first_created_on',
            new_name='firstcreated',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='last_editted_on',
            new_name='lasteditted',
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
