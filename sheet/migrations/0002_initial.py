# Generated by Django 4.0.1 on 2022-02-10 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sheet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sheet',
            name='style',
            field=models.ManyToManyField(to='sheet.Style'),
        ),
        migrations.AddField(
            model_name='sheet',
            name='tonality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sheet.tonality'),
        ),
        migrations.AddField(
            model_name='sheet',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sheet.type'),
        ),
    ]