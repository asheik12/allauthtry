# Generated by Django 2.2.5 on 2019-10-23 07:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('testperm', '0002_auto_20191023_1140'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='employee',
            managers=[
                ('emp', django.db.models.manager.Manager()),
            ],
        ),
    ]
