# Generated by Django 3.1 on 2020-10-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='pizza_name',
            field=models.CharField(default='lindaaa', max_length=500),
            preserve_default=False,
        ),
    ]
