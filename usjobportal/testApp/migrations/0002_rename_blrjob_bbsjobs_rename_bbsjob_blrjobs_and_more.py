# Generated by Django 4.0.5 on 2022-06-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blrjob',
            new_name='bbsjobs',
        ),
        migrations.RenameModel(
            old_name='bbsjob',
            new_name='blrjobs',
        ),
        migrations.RenameModel(
            old_name='hydjob',
            new_name='hydjobs',
        ),
    ]