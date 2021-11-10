# Generated by Django 3.2.7 on 2021-10-09 06:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deckapp', '0013_alter_deck_group_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='DeckRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('is_accepted', models.BooleanField(default=False)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck', to='deckapp.deck')),
                ('requesting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
