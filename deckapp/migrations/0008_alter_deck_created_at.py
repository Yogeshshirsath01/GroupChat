# Generated by Django 3.2.7 on 2021-10-02 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deckapp', '0007_auto_20211001_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
