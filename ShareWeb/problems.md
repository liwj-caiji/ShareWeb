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