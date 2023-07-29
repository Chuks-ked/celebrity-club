# Generated by Django 4.2.1 on 2023-07-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_meetup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fancard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('option_one', models.CharField(max_length=100)),
                ('option_two', models.CharField(max_length=100)),
                ('recommend', models.BooleanField(default=False)),
            ],
        ),
    ]
