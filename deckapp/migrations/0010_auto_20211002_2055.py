# Generated by Django 3.2.7 on 2021-10-02 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deckapp', '0009_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
