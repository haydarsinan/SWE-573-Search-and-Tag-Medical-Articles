# Generated by Django 3.2.4 on 2021-06-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchAndTag', '0002_auto_20210616_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Authors',
            field=models.ManyToManyField(blank=True, to='searchAndTag.Authors'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='PubmedID',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='authors',
            name='Name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='authors',
            name='Surname',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='keywords',
            name='Keyword',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='tags',
            name='Tag',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='users',
            name='Articles',
            field=models.ManyToManyField(blank=True, to='searchAndTag.Articles'),
        ),
    ]
