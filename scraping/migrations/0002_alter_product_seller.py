# Generated by Django 4.1.3 on 2022-11-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="seller",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
