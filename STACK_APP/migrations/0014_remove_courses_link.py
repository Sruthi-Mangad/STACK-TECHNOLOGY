# Generated by Django 5.0.2 on 2024-05-16 11:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("STACK_APP", "0013_courses_link"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="courses",
            name="link",
        ),
    ]
