# Generated by Django 2.0.5 on 2018-08-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='title',
            field=models.TextField(default='', null=True),
        ),
    ]
