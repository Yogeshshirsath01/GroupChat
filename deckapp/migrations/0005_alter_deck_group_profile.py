# Generated by Django 3.2.7 on 2021-09-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deckapp', '0004_deck_group_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='group_profile',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
