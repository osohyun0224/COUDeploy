# Generated by Django 2.2.28 on 2022-08-16 07:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20220513_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grass',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='problem_sequence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), blank=True, default=list, size=None),
        ),
    ]