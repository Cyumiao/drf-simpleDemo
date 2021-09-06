from django.db import models

class Category(models.Model):
  name = models.CharField(verbose_name='分类', max_length=10)

  def __str__(self) -> str:
      return self.name;

class Tag(models.Model):
  name = models.CharField(verbose_name='标签', max_length=10)

  def __str__(self) -> str:
    return self.name

class Article(models.Model):
  title = models.CharField(verbose_name='标题', max_length=30)
  content = models.TextField(verbose_name='内容')
  views_num = models.IntegerField(verbose_name='查看次数')
  category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, verbose_name='标签')
  author_name = models.CharField(verbose_name='发布人', max_length=20)
  author_tel = models.CharField(verbose_name='发布人手机号', max_length=13)
