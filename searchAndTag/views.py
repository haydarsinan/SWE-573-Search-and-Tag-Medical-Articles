from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .userCreationForm import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from searchAndTag.models import Authors,Articles,Tags,Keywords,Users


# Create your views here.

def homePage(request):
    return render(request, 'searchAndTag/homePage.html')


def searchPage(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        articleSearched = Articles.objects.filter(Title__icontains=searched) | Articles.objects.filter(Abstract__icontains=searched) | Articles.objects.filter(Tags__Tag__icontains=searched)
        return render(request, 'searchAndTag/searchPage.html', {'searched': searched, 'articleResult': articleSearched})
    else:
        return render(request, 'searchAndTag/searchPage.html')


def tagPage(request):
    return render(request, 'searchAndTag/tagPage.html')

def resultsPage(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        articleSearched = Articles.objects.filter(Title__icontains=searched) | Articles.objects.filter(Abstract__icontains=searched) | Articles.objects.filter(Tags__Tag__icontains=searched)
        return render(request, 'searchAndTag/searchResults.html', {'searched': searched, 'articleResult': articleSearched})
    else:
        return render(request, 'searchAndTag/searchResults.html')


def articlePage(request, article_id):
    article_list=Articles.objects.filter(id__exact=article_id)
    return render(request, 'searchAndTag/articlePage.html', {'article': article_list})

def addTag(request, article_id):
    if request.method == "POST":
        tagV = request.POST.get('searchedTag')
        linkV = request.POST.get('searchedWiki')
        tag = Tags(Tag=tagV, Link=linkV)
        tag.save()
        article = Articles.objects.get(pk=article_id)
        article.Tags.add(tag)
        return render(request, 'searchAndTag/taggingPage.html')
    else:
        return render(request, 'searchAndTag/taggingPage.html')


def accountPage(request):
    return render(request, 'searchAndTag/accountPage.html')


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="searchAndTag/loginPage.html", context={"login_form": form})


def registerPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration is successful!")
            return redirect("homepage")
        messages.error(request, "Registration is failed")
    form = NewUserForm
    return render(request=request, template_name="searchAndTag/registerPage.html", context={"register_form": form})
