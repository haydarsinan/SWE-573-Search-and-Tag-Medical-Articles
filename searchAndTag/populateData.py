from searchAndTag.models import Articles, Authors, Keywords, Tags

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

mytree = ET.parse('listOfArticles.xml')
myroot = mytree.getroot()

# count = 0
# for article in myroot:
#     for PMID in article.iter("PMID"):
#         print(PMID.text)
#     for ArticleTitle in article.iter("ArticleTitle"):
#         print(ArticleTitle.text)
#     PubDate = article[0][1]
#     for year in PubDate.iter("Year"):
#         print(year.text, end="-")
#     for month in PubDate.iter("Month"):
#         print(month.text, end="-")
#     for day in PubDate.iter("Day"):
#         print(day.text)
#     for Abstract in article.iter("AbstractText"):
#         print(Abstract.text)
#     for Author in article.iter("Author"):
#         for Name in Author.iter("ForeName"):
#             print(Name.text, end=" ")
#         for SurName in Author.iter("LastName"):
#             print(SurName.text)
#     for Keyword in article.iter("Keyword"):
#         print(Keyword.text)
#     for ArticleId in article.iter("ArticleIdList"):
#         for DOI in ArticleId:
#             idType = (DOI.get('IdType'))
#             if idType == 'doi':
#                 print(DOI.text)
#     print("\t")
# print(count)
#

for article in myroot:
    for PMID in article.iter("PMID"):
        pmid= PMID.text
    for ArticleTitle in article.iter("ArticleTitle"):
        articletittle = ArticleTitle.text
    PubDate = article[0][1]
    for year in PubDate.iter("Year"):
        yearV = year.text
    for month in PubDate.iter("Month"):
        monthV = month.text
    for day in PubDate.iter("Day"):
        dayV = day.text
    pubdate = dayV + "-" + monthV + "-" + yearV
    for Abstract in article.iter("AbstractText"):
        abstract = Abstract.text
    for ArticleId in article.iter("ArticleIdList"):
        for DOI in ArticleId:
            idType = (DOI.get('IdType'))
            if idType == 'doi':
                doi = DOI.text
    article = Articles(PubmedID=pmid, Title=articletittle, PubDate=pubdate, Abstract=abstract, Doi=doi)
    article.save()
    for Author in article.iter("Author"):
        for Name in Author.iter("ForeName"):
            nameV = Name.text
        for SurName in Author.iter("LastName"):
            surnameV = SurName.text
        author = Authors(Name=nameV, Surname=surnameV)
        author.save()
        article.Authors.add(author)
    for Keyword in article.iter("Keyword"):
        keyword = Keywords(Keyword=Keyword.text)
        keyword.save()
        article.Keywords.add(keyword)


