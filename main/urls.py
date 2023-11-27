from django.urls import path

from . import views
from .views import *
urlpatterns = [
    path('', views.register, name = 'register'),
    path('api/v1/adduser/', UserApiAdd.as_view()),
    path('api/v1/book/', BookApiList.as_view()),
    path('api/v1/book/<int:pk>/', BookApiDetailView.as_view()),
]