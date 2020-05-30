

from django.urls import path
from .           import views
app_name = "articles"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/add/', views.add, name='add'),
    path('<int:article_id>/details/', views.details, name='details'),
]
