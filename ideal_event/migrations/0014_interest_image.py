# Generated by Django 2.1.5 on 2019-01-09 01:36

from django.db import migrations, models
import ideal_event.models


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_event', '0013_auto_20190108_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=ideal_event.models.upload_location, width_field='width_field'),
        ),
    ]
