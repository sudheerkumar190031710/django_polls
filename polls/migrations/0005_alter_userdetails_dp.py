# Generated by Django 4.0.4 on 2022-07-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_pollquestions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='dp/'),
        ),
    ]