# Generated by Django 2.1.4 on 2018-12-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slackforms', '0010_auto_20181213_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='endpoint',
            field=models.ForeignKey(blank=True, help_text='A URL to hit with the processed and validated form data.', null=True, on_delete=django.db.models.deletion.PROTECT, to='slackforms.Endpoint'),
        ),
    ]
