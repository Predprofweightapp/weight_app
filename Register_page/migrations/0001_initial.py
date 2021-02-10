# Generated by Django 3.1.6 on 2021-02-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.EmailField(max_length=254, verbose_name='mail')),
                ('password', models.CharField(max_length=10, verbose_name='password')),
            ],
        ),
    ]