# Generated by Django 2.1.4 on 2018-12-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackforms', '0006_auto_20181204_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='argument_prop_name',
        ),
        migrations.AddField(
            model_name='form',
            name='data_source',
            field=models.CharField(blank=True, help_text='\nThe source of data if an Id is supplied. {id} variable passed through. See docs.\n', max_length=40, null=True, unique=True),
        ),
    ]
