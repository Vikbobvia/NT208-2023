# Generated by Django 3.2.19 on 2023-09-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_table',
            name='description',
            field=models.TextField(max_length=30000000000000),
        ),
    ]
