# Generated by Django 4.1 on 2022-11-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppTwo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=264),
        ),
    ]
