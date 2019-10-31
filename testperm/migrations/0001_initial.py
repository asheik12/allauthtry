# Generated by Django 2.2.5 on 2019-10-23 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('doj', models.DateField(default=datetime.date(2019, 10, 23))),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
