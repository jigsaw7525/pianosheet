# Generated by Django 4.0.1 on 2022-02-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='point',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='respondent',
        ),
        migrations.AddField(
            model_name='profile',
            name='nickename',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Respondent',
        ),
    ]
