# Generated by Django 2.2.3 on 2020-01-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminTransaction',
            fields=[
                ('to', models.CharField(editable=False, max_length=39, primary_key=True, serialize=False)),
                ('by', models.CharField(editable=False, max_length=39)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
