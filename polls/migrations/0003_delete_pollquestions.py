# Generated by Django 4.0.4 on 2022-07-07 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_pollquestions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PollQuestions',
        ),
    ]
