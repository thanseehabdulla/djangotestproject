from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('test/<pk>/', views.TestView.as_view(), name="test")

]
