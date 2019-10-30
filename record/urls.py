from django.urls import path

from . import views

app_name = 'record'
urlpatterns = [
    path('', views.index_record, name='indexRecord'),
]
