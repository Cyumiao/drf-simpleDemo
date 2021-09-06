### 项目简介及运行

用最基础的DRF机制编写的接口，仅使用序列化及视图类。

##### 开发环境

| 名称  | 说明  |
|:----------|:----------|
| 操作系统    | macOS Catalina v10.15.5    |
| 开发工具    | vscode：v1.60.0 (Universal)    |
| python版本    | 3.8    |
| Django版本    | 3.2.6    |
| DRF版本    | 3.12.4    |

##### 运行项目

> git clone https://github.com/Cyumiao/drf-simpleDemo

sudo pip3 install -Ur requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 8889

### 调试接口

| 接口名称  | method  | url  |
| ------------ | ------------ | ------------ |
| 新增标签Tag  | POST  | http://127.0.0.1:8889/api/tags/  |
| 获取标签Tag | GET  | http://127.0.0.1:8889/api/tags/  |
| 获取某个标签Tag  | GET  | http://127.0.0.1:8889/api/tag/1  |
| 更新某个标签Tag | PUT  | http://127.0.0.1:8889/api/tag/1/  |
| 删除某个标签Tag  | DELETE  | http://127.0.0.1:8889/api/tag/1/  |
| 新增分类Category  | POST  | http://127.0.0.1:8889/api/categorys/  |
| 获取分类Category  | GET  | http://127.0.0.1:8889/api/categorys/  |
| 获取某个分类Category  | GET  | http://127.0.0.1:8889/api/category/1  |
| 更新某个分类Category  | PUT  | http://127.0.0.1:8889/api/category/1/  |
| 删除某个分类Category  | DELETE  | http://127.0.0.1:8889/api/category/1/  |
| 新增文章Article  | POST  | http://127.0.0.1:8889/api/article/add/ |
| 获取文章Article  | GET  | http://127.0.0.1:8889/api/articles/ |
| 获取某个文章Article   | GET  | http://127.0.0.1:8889/api/article/1  |
| 更新某个文章Article   | PUT  | http://127.0.0.1:8889/api/article/1 |
| 删除某个文章Article   | DELETE  | http://127.0.0.1:8889/api/article/1 |

### 相关博客
相关博客：[https://www.xinghuijin.com/detail/95](https://www.xinghuijin.com/detail/95 "点击查看")