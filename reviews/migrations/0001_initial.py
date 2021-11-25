# Generated by Django 3.2.9 on 2021-11-24 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gins', '0003_rename_hasvisitorcetre_distillery_hasvisitorcentre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('first_created_on', models.DateTimeField(auto_now_add=True)),
                ('last_editted_on', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gins.distillery')),
            ],
        ),
    ]