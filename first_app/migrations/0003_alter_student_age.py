# Generated by Django 5.1.1 on 2024-11-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_student_age_alter_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
