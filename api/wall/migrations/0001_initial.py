# Generated by Django 2.0.4 on 2018-04-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
    ]
