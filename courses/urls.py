from django.urls import path
from .views import (
            CourseView,
            CourseListView,
            CourseCreateView,
            CourseUpdateView,
            # my_fbv,
        )

app_name = 'courses'
urlpatterns = [
    # path('', CourseView.as_view(template_name = 'contact.html'), name='courses-list'),
    # path('', my_fbv, name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('', CourseListView.as_view(), name='courses-list'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path(
        '<int:id>/update/',
        CourseUpdateView.as_view(),
        name='courses-update'
        ),
]
