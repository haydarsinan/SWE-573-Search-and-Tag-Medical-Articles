import sys
import requests
import xmltodict
import entrezpy.esearch.esearcher

# url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=asthma+children+AND+(Review%205Bptyp]+AND+%22loattrfree+full+text%22[sb])"
# response = requests.get(url)
# data = xmltodict.parse(response.content)

e = entrezpy.esearch.esearcher.Esearcher('esearcher', 'email')
a = e.inquire({'db': 'pubmed', 'term': 'breast cancer', 'retmax': 45000, 'rettype': 'uilist'})
print(a.get_result().uids)
idlist = a.get_result().uids
print(idlist)
import entrezpy.efetch.efetcher

e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)

# sys.stdout = open("listOfArticles.xml", "w")
#
# analyzer = e.inquire({'db': 'pubmed',
#                       'id': idlist,
#                       'retmode': 'xml',
#                       'rettype': 'abstract'})
#
# sys.stdout.close()

#xmlmerge package is used to merge these xml files because one time fetcing got error because of huge data

sys.stdout = open("listOfArticles1.xml", "w")
fiveklot = idlist[0:3000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles2.xml", "w")
fiveklot = idlist[3000:6000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles3.xml", "w")
fiveklot = idlist[6000:9000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles4.xml", "w")
fiveklot = idlist[9000:12000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles5.xml", "w")
fiveklot = idlist[12000:15000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles6.xml", "w")
fiveklot = idlist[15000:18000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles7.xml", "w")
fiveklot = idlist[18000:21000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles8.xml", "w")
fiveklot = idlist[21000:24000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles9.xml", "w")
fiveklot = idlist[24000:27000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles10.xml", "w")
fiveklot = idlist[27000:30000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles11.xml", "w")
fiveklot = idlist[30000:33000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles12.xml", "w")
fiveklot = idlist[33000:36000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles13.xml", "w")
fiveklot = idlist[36000:39000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles14.xml", "w")
fiveklot = idlist[39000:42000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()


sys.stdout = open("listOfArticles15.xml", "w")
fiveklot = idlist[42000:45000]
e = entrezpy.efetch.efetcher.Efetcher('applicationMine',
                                      'haydarsinanyildirim@gmail.com',
                                      apikey="6cb3405a9a9e4058723f254ed8967a71fa08",
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)
e.inquire({'db': 'pubmed',
                  'id': fiveklot,
                  'retmode': 'xml',
                  'rettype': 'abstract'})
sys.stdout.close()