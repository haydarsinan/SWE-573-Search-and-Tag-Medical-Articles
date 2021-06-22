from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('home/', views.homePage, name='homepage'),
    path('search/', views.searchPage, name='searchpage'),
    path('tags/', views.tagPage, name='tagpage'),
    path('results/', views.resultsPage, name='resultpage'),
    path('article/<int:article_id>/', views.articlePage, name='articlepage'),
    path('addtag/<int:article_id>/', views.addTag, name='taggingpage'),

    path('account/', views.accountPage, name='accountpage'),
    path('login/', views.loginPage, name='loginpage'),
    path('register/', views.registerPage, name='registerpage'),
]

#
# from searchAndTag.models import Articles, Authors, Keywords, Tags
#
# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET
# mytree = ET.parse('searchAndTag/listOfArticles.xml')
# myroot = mytree.getroot()
#
#
# for article in myroot:
#     for PMID in article.iter("PMID"):
#         pmid= PMID.text
#     for ArticleTitle in article.iter("ArticleTitle"):
#         articletittle = ArticleTitle.text
#     PubDate = article[0][1]
#     for year in PubDate.iter("Year"):
#         yearV = year.text
#     for month in PubDate.iter("Month"):
#         monthV = month.text
#     for day in PubDate.iter("Day"):
#         dayV = day.text
#     pubdate = dayV + "-" + monthV + "-" + yearV
#     for Abstract in article.iter("AbstractText"):
#         abstract = Abstract.text
#     for ArticleId in article.iter("ArticleIdList"):
#         for DOI in ArticleId:
#             idType = (DOI.get('IdType'))
#             if idType == 'doi':
#                 doi = DOI.text
#     articledb = Articles(PubmedID=pmid, Title=articletittle, PubDate=pubdate, Abstract=abstract, Doi=doi)
#     articledb.save()
#     for AuthorV in article.iter("Author"):
#         for Name in AuthorV.iter("ForeName"):
#             nameV = Name.text
#         for SurName in AuthorV.iter("LastName"):
#             surnameV = SurName.text
#         author = Authors(Name=nameV, Surname=surnameV)
#         author.save()
#         articledb.Authors.add(author)
#     for Keyword in article.iter("Keyword"):
#         keyword = Keywords(Keyword=Keyword.text)
#         keyword.save()
#         articledb.Keywords.add(keyword)
