# Generated by Django 5.1.3 on 2024-11-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='dominant_hand',
            field=models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], default='Right', max_length=20),
        ),
        migrations.AddField(
            model_name='player',
            name='focus',
            field=models.CharField(choices=[('Technique', 'Technique'), ('Strategy', 'Strategy'), ('Speed', 'Speed'), ('Fitness', 'Fitness'), ('Concentration', 'Concentration')], default='Technique', max_length=20),
        ),
        migrations.AddField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=20),
        ),
    ]