# Generated by Django 3.2.19 on 2023-09-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text_table',
            fields=[
                ('date', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
