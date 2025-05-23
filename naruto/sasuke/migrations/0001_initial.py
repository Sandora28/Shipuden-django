# Generated by Django 5.1.3 on 2025-05-19 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jutsu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Ninjutsu', 'Ninjutsu'), ('Genjutsu', 'Genjutsu'), ('Taijutsu', 'Taijutsu')], max_length=20)),
                ('chakra_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rank', models.CharField(choices=[('Genin', 'Genin'), ('Chunin', 'Chunin'), ('Jonin', 'Jonin')], max_length=100)),
                ('clan', models.CharField(max_length=50)),
                ('chakra_nature', models.CharField(max_length=50)),
                ('jutsu', models.ManyToManyField(blank=True, to='sasuke.jutsu')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rank', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=10)),
                ('assigned_to', models.ManyToManyField(to='sasuke.ninja')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_leader', to='sasuke.ninja')),
            ],
        ),
        migrations.AddField(
            model_name='ninja',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sasuke.team'),
        ),
    ]
