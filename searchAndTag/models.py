from django.db import models
from django.db.models import ManyToManyField
from django.db.models import ForeignKey
from django.db.models import OneToOneField


# Create your models here.


class Keywords(models.Model):
    Keyword = models.CharField(max_length=300, blank=True, null=True)

    # def __str__(self):
    #     return self.Keyword

    class Meta:
        verbose_name_plural = "Keywords"


class Authors(models.Model):
    Name = models.CharField(max_length=300,blank=True, null=True)
    Surname = models.CharField(max_length=300, blank=True, null=True)
    Affiliation = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.Name + ' ' + self.Surname

    class Meta:
        verbose_name_plural = "Authors"


class Tags(models.Model):
    Tag = models.CharField(max_length=300)
    Link = models.URLField(blank=True, null=True)

    # def __str__(self):
    #     return self.Tag

    class Meta:
        verbose_name_plural = "Tags"


class Articles(models.Model):
    PubmedID = models.CharField(max_length=300, blank=True, null=True)
    Title = models.TextField(blank=True, null=True)
    PubDate = models.CharField(max_length=300, blank=True, null=True)
    Abstract = models.TextField(blank=True, null=True)
    Doi = models.URLField(blank=True, null=True)

    Keywords = ManyToManyField(Keywords, blank=True)
    Authors = ManyToManyField(Authors, blank=True, null=True)
    Tags = ManyToManyField(Tags, blank=True, null=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = "Articles"


class Users(models.Model):
    Username = models.CharField(max_length=120)
    Password = models.CharField(max_length=120)
    Email = models.EmailField()
    Articles = ManyToManyField(Articles, blank=True)
    Tag = ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.Username

    class Meta:
        verbose_name_plural = "Users"
