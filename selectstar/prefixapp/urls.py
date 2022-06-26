from django.urls import path

from . import views

urlpatterns = [
    path('prefix_data', views.PrefixList.as_view())
]