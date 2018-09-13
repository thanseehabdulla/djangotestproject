from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('page', views.page, name='page'),
    path('display', views.display, name='page'),
    path('vote/<int:question_id>', views.vote, name='votess'),
    path('test/<pk>/', views.TestView.as_view(), name="test"),

]
