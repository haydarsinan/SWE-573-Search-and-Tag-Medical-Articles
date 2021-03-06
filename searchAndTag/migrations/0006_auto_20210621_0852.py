# Generated by Django 3.2.4 on 2021-06-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchAndTag', '0005_auto_20210620_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Authors',
            field=models.ManyToManyField(blank=True, to='searchAndTag.Authors'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='PubDate',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='authors',
            name='Affiliation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='Surname',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='keywords',
            name='Keyword',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Articles',
            field=models.ManyToManyField(blank=True, to='searchAndTag.Articles'),
        ),
    ]
