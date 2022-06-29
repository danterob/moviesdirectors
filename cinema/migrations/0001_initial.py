# Generated by Django 4.0.5 on 2022-06-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el genero', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ingrese el titulo', max_length=60)),
                ('description', models.TextField(blank=True, help_text='Ingrese una breve descripción', null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('genre', models.ManyToManyField(to='cinema.genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrt_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('born_date', models.DateField(blank=True, null=True)),
                ('movie', models.ManyToManyField(blank=True, to='cinema.movies')),
            ],
        ),
    ]