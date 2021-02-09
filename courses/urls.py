from django.urls import path
from .views import (
            my_fbv
        )

app_name = 'courses'
urlpatterns = [
    path('', my_fbv, name='courses-list'),
]
