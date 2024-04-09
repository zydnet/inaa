# Generated by Django 4.2.7 on 2024-04-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('subject', models.CharField(max_length=122)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
