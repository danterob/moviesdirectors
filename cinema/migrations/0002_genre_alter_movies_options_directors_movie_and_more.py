# Generated by Django 4.0.5 on 2022-06-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el genero', max_length=64)),
            ],
        ),
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='directors',
            name='movie',
            field=models.ManyToManyField(to='cinema.movies'),
        ),
        migrations.AddField(
            model_name='movies',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(to='cinema.genre'),
        ),
    ]