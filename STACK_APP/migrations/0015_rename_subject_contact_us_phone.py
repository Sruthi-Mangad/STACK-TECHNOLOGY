# Generated by Django 5.0.2 on 2024-06-01 11:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("STACK_APP", "0014_remove_courses_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact_us",
            old_name="subject",
            new_name="phone",
        ),
    ]
