from django.shortcuts import render, get_object_or_404
from django.http  import HttpResponse, Http404
import datetime
from django.template import loader
from .models import Article, Author
def index(request):
    articles_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('articles/index.html')
    context = { 'articles_list':articles_list  }
    return HttpResponse(template.render(context, request))

def details(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    #try:
    #     article = Article.objects.get(pk=article_id)
    #except Article.DoesNotExist:
    #       raise Http404("Article Does not exist")

    return render(request, 'articles/details.html',{'article':article} )
    #return HttpResponse("You're looking at Article %s." %article_id)


def add(request, article_id):
    response = "Article Number %s  added to list"
    return HttpResponse(response % article_id)

# Create your views here.
