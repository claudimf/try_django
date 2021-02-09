from django.urls import path

from .views import (
                    ArticleDetailView,
                    ArticleListView
                    )

app_name = 'articles'
urlpatterns = [
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('', ArticleListView.as_view(), name='article-list')
]
