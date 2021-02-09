from django.urls import path

from .views import (
                    article_detail_view,
                    article_list_view
                    )

app_name = 'articles'
urlpatterns = [
    path('<int:id>/', article_detail_view, name='article-detail'),
    path('', article_list_view, name='article-list')
]
