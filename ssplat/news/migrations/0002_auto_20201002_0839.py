# Generated by Django 3.1.2 on 2020-10-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='url_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]