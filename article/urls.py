from django.urls import path
from .views import *

urlpatterns = [
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tag/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('categorys/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('article/add/', ArticleAdd.as_view(), name='article-add'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail')
]
