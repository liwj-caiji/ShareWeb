# 项目介绍
## 环境配置
python3 
django 3.2.8
## 项目介绍
一个简单的可以说是类似博客的网站,用户可以发表文章,依据标题或作者信息去查看其他用户的文章

## 项目运行准备
- 安装django 3.2.8
- 安装mysql 8.*,修改ShareWeb中的数据库配置信息(对应的数据库需要自己先创建,确保对应数据库存在并且可以本地登录上数据库)
- 在manage.py所在目录下执行下列代码
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```
上述代码成功运行则浏览器访问127.0.0.1:8000/user/login即可

前端页面手写的,有点点不太美观,不过勉强还能看,关于写项目时遇到的部分问题记录在problems.md

## 项目目录设计
本项目基于django框架实现,前后端未分离,包含的app有user和article
各app目录下文件的内容:
- urls.py 路由信息
- view 视图函数实现
- models.py 模型信息
- *_form.py 表单信息
- decoration.py 装饰器
- migrations 数据库迁移信息

static目录下的是静态文件,包含CSS和Js(包含collectstatic的结果)
templates 放置模板信息

<a href="http://www.lwjcyh.com:8000/user/login" target="_blank">样例</a>

<a href="http://c.biancheng.net/django/" target="_blank"> 适合入门的django教程</a>