# Generated by Django 3.0.8 on 2020-08-07 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acccounts', '0004_auto_20200719_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user1',
        ),
    ]
