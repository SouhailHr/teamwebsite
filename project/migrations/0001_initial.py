# Generated by Django 3.2.18 on 2023-04-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('overview', models.TextField(max_length=500)),
                ('title', models.CharField(max_length=100)),
                ('tools', models.CharField(max_length=200)),
                ('Link', models.CharField(max_length=200)),
                ('dashbord_image', models.ImageField(max_length=255, upload_to='images/%y/%m/%d/')),
            ],
        ),
    ]