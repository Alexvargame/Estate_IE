# Generated by Django 5.0.7 on 2025-06-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_alter_property_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertytype',
            name='transcription',
            field=models.CharField(default='', max_length=100),
        ),
    ]
