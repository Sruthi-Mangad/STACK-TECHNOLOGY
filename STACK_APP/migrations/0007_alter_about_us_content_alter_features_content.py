# Generated by Django 5.0.2 on 2024-05-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("STACK_APP", "0006_remove_courses_offer_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about_us",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="features",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
    ]
