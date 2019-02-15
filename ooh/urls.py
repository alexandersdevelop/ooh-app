from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    path('<str:campaign>', views.detail, name='detail'),
    path('save/save_changes/', views.save, name='save'),
]