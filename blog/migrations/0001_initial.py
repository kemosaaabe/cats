# Generated by Django 4.0.3 on 2022-03-18 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Порода')),
                ('text', models.TextField(verbose_name='Описание породы')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Породы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Кличка')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.breed', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Котик',
                'verbose_name_plural': 'Котики',
                'ordering': ['name'],
            },
        ),
    ]
