# Generated by Django 4.1.1 on 2022-10-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]