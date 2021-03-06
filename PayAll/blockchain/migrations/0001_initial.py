# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-20 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('index', models.IntegerField()),
                ('_hash', models.CharField(max_length=100)),
                ('previousHash', models.CharField(max_length=100)),
                ('nounce', models.IntegerField()),
                ('difficulty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocks', models.ManyToManyField(to='blockchain.Block')),
            ],
        ),
        migrations.CreateModel(
            name='pendingTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromAdd', models.CharField(max_length=100)),
                ('toAdd', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='pendingtransactions',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blockchain.Transaction'),
        ),
        migrations.AddField(
            model_name='block',
            name='transactions',
            field=models.ManyToManyField(blank=True, null=True, to='blockchain.Transaction'),
        ),
    ]
