# Generated by Django 3.2.4 on 2021-06-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchAndTag', '0003_auto_20210616_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='keywords',
            options={'verbose_name_plural': 'Keywords'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='tags',
            name='Link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='Authors',
            field=models.ManyToManyField(blank=True, to='searchAndTag.Authors'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Articles',
            field=models.ManyToManyField(blank=True, to='searchAndTag.Articles'),
        ),
    ]
