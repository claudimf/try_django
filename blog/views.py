from django.shortcuts import render, get_object_or_404
from .models import Article

from django.views.generic import (
    DetailView,
    ListView
)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    # '<blog>/<modelname>_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


# # Old way
# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, "articles/article_detail.html", context)


# def article_list_view(request):
#     query_set = Article.objects.all()
#     context = {
#         'object_list': query_set
#     }
#     return render(request, "articles/article_list.html", context)
