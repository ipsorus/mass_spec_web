# Generated by Django 4.1.7 on 2023-04-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_spectrummeasurement_spectrumpeak_spectrumfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spectrumfield',
            name='key',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='spectrumfield',
            name='value',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
