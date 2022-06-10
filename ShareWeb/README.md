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

<a href="http://www.lwjcyh.com:8000/user/login" target="_blank">样例</a>
