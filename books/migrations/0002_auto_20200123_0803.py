# Generated by Django 3.0.2 on 2020-01-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.AddField(
            model_name='author',
            name='internet',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
