from rest_framework import generics
from .models import *
from .serializers import *

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
class ArticleAdd(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleOperateSerializer
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleOperateSerializer