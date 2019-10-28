from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('account.urls')),
    path('record/', include('record.urls')),
    path('result/', include('result.urls')),
]
