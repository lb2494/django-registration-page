# Generated by Django 2.1 on 2018-10-10 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20181010_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='picture',
            new_name='profile_pic',
        ),
    ]
