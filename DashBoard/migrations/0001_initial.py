# Generated by Django 3.0.3 on 2020-03-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VulnerableLibraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vulnerability', models.TextField()),
                ('Package', models.TextField()),
                ('Package_Link', models.TextField()),
                ('Version', models.TextField()),
                ('Overview', models.TextField()),
            ],
        ),
    ]
