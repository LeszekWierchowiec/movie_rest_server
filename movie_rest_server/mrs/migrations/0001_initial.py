# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
                ('ranking', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '*****'), (5, '******')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('ranking', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '*****'), (5, '******')], null=True)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=64)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrs.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrs.Person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(through='mrs.Role', to='mrs.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_director', to='mrs.Person'),
        ),
    ]
