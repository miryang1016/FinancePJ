from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.article_list_create, name = 'article_list_create'),
    path('comments/', views.comment_list_create, name = 'comment_list_create'),
    path('<int:article_pk>/delete/', views.delete, name = 'delete'),
    path('articles/<int:article_pk>/', views.article_detail, name = 'article_detail'),
    path('comments/<int:comment_pk>/', views.comment_detail, name = 'comment_detail'),
    path('articles/<int:article_id>/comments/', views.article_comments, name='article_comments'),
]