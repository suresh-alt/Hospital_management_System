# Generated by Django 3.0.7 on 2020-12-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_doctormodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('Test_No', models.AutoField(primary_key=True, serialize=False)),
                ('Test_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
