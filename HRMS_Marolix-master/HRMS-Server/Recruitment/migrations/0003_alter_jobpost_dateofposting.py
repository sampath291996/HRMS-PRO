# Generated by Django 4.2.1 on 2023-07-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment', '0002_alter_jobpost_dateofposting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='dateOfPosting',
            field=models.TextField(),
        ),
    ]
