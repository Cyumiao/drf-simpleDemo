# Generated by Django 3.2.6 on 2021-09-06 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('views_num', models.IntegerField(verbose_name='查看次数')),
                ('author_name', models.CharField(max_length=20, verbose_name='发布人')),
                ('author_tel', models.CharField(max_length=13, verbose_name='发布人手机号')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.category', verbose_name='分类')),
                ('tags', models.ManyToManyField(to='article.Tag', verbose_name='标签')),
            ],
        ),
    ]