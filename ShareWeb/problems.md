# 遇到的问题

1. css 样式引入问题
+ base.html 引入base.css, base.css引入user.css, 导入的user_login.cs和user_register.css,其中的user_register的CSS样式不起效 

- 解决方法 : html的head中添加 <base href="/">

2. 修改css样式后,页面无变化
- 解决方法 : 清楚浏览器的缓存

3. 导入其他app的model时路径报错
- 解决方法 : from app_name.models import *

4. 使用自定义装饰器时出现view must be a callable or a list...
- 解决方法 : 自定义的装饰器缺少返回值

5. form表单POST后回到/目录
- 解决方法 : 将form中的action从"."改为""

6. url路径不匹配 和 函数缺少参数
- 解决方法 : urls.py中的path路径最后缺少个/  查看匹配变量名是否一致

7. mysql : Can't connect to MySQL server on 'localhost'
解决方法 : Win 搜索 服务, 打开MySQL服务

8. Could not parse the remainder: '/article.title' from 'article.author_name/article.title'
解决方法 : {% url ' url_name' }中传参数时需要以空格分开, {% url 'article_read' article.author_name  article.title %}这样向url中传入两个参数,形式为article_read/article.author_name/article.title/

9. 搜索页面的header处超链接无法点击
解决办法 : 更改search-body的大小，无法点击是search-body覆盖了header

10. 用上传的背景图片替换默认背景 background: url( {% static 'media' %} {{cur_user_images.avatar_image.url}})该写法不行
                                           url('{{cur_user_images_background_url}}')也不行 