# Generated by Django 2.2.28 on 2022-08-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAuthentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(null=True)),
                ('verify_email_token', models.TextField(null=True)),
                ('verify_email_token_expire_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'emailauthentication',
            },
        ),
    ]