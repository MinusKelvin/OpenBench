# Generated by Django 4.2.1 on 2024-05-13 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenBench', '0003_manual_ob_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='genfens_args',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='test',
            name='play_reverses',
            field=models.BooleanField(default=False),
        ),
    ]