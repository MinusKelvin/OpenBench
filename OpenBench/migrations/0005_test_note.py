# Generated by Django 4.2.1 on 2024-10-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenBench', '0004_test_genfens_args_test_play_reverses'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='note',
            field=models.TextField(default=''),
        ),
    ]
