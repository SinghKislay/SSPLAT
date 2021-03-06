# Generated by Django 3.1.2 on 2020-10-02 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=50, unique=True)),
                ('source_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('Desc', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('url_image', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=10000)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.articlesource')),
            ],
        ),
    ]
