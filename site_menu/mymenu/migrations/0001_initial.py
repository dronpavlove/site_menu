# Generated by Django 4.0 on 2023-03-01 15:26

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='mymenu.categorymenu', verbose_name='Родительская категория меню')),
            ],
            options={
                'verbose_name': 'Категория меню',
                'verbose_name_plural': 'Категории меню',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='PodCategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150)),
                ('categori_url', models.TextField(verbose_name='Ссылка')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='mymenu.categorymenu', verbose_name='Категория меню')),
            ],
            options={
                'verbose_name': 'Подпункт меню',
                'verbose_name_plural': 'Подпункты меню',
            },
        ),
    ]
