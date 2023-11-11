# Generated by Django 4.2.7 on 2023-11-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('note', models.TextField(max_length=400)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]