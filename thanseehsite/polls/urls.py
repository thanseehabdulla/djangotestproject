from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('page', views.page, name='page'),
    path('display', views.display, name='page'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('details/<int:question_id>', views.details, name='details'),
    path('voteme/<int:question_id>', views.voteme, name='voteme'),
    path('test/<pk>/', views.TestView.as_view(), name="test"),

]
