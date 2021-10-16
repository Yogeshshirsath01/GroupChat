# Generated by Django 3.2.7 on 2021-10-12 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deckapp', '0015_delete_deckrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(max_length=500)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck', to='deckapp.deck')),
            ],
        ),
    ]
