from django.db.models import fields
from rest_framework import serializers
import re
from .models import *

# 分类的序列化
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

# 标签的序列化
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('id', 'name')

# 文章获取的序列化
class ArticleListSerializer(serializers.ModelSerializer):
  tag_count = serializers.SerializerMethodField() # 标签个数
  category = CategorySerializer()
  tags = TagSerializer(many=True)

  class Meta:
    model = Article
    fields = '__all__'

  def get_tag_count(self, obj):
    return obj.tags.count();


# 文章添加/更新/删除的序列化
class ArticleOperateSerializer(serializers.ModelSerializer):
  title = serializers.CharField(max_length=30, required=True, min_length=6, error_messages={
    'max_length': '标题长度不可以超过30字',
    'min_length': '标题长度不可以少于6字',
    'required': '标题不能为空'
  })
  content = serializers.CharField(required=True, error_messages={
    'required': '内容不能为空'
  })
  author_name = serializers.CharField(max_length=20, required=True, error_messages={
    'required': '内容不能为空',
    'max_length': '发布人不可以超过20字'
  })
  class Meta:
    model = Article
    fields = '__all__'
  def validate_author_tel(self, author_tel):
    if not re.match(r'1[3456789]\d{9}', author_tel):
        raise serializers.ValidationError('手机号不合法')
    return author_tel