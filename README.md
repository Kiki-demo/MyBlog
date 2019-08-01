# KFitBlog
K健身俱乐部博客
## 在本地运行项目

1. 安装项目依赖

   如果使用了虚拟环境，确保激活并进入了虚拟环境，在命令行进入项目所在的 django-blog-tutorial 文件夹，运行如下命令：

   ```
   pip install -r requirements.txt
   ```

2. 迁移数据库

   在上一步所在的位置运行如下命令迁移数据库：

   ```
   python manage.py migrate
   ```

3. 创建后台管理员账户

   在上一步所在的位置运行如下命令创建后台管理员账户

   ```
   python manage.py createsuperuser
   ```


4. 运行开发服务器

   在上一步所在的位置运行如下命令开启开发服务器：

   ```
   python manage.py runserver
   ```

   在浏览器输入：127.0.0.1:8000

5. 进入后台发布文章

   在浏览器输入：127.0.0.1:8000/admin

   使用第 5 步创建的后台管理员账户登录


