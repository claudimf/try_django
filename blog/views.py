from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object': obj
    }
    return render(request, "articles/article_detail.html", context)


def article_list_view(request):
    query_set = Article.objects.all()
    context = {
        'object_list': query_set
    }
    return render(request, "articles/article_list.html", context)
