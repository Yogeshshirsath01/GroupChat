# Generated by Django 3.2.7 on 2021-10-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deckapp', '0012_alter_deck_group_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='group_profile',
            field=models.ImageField(default='uploads/groupofpeople.png', upload_to='uploads/'),
        ),
    ]
