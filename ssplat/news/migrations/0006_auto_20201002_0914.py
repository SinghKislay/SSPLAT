# Generated by Django 3.1.2 on 2020-10-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201002_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
