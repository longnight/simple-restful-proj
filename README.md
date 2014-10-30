simple-restful-proj
===================

A simple restful api sample, build with Django.

环境：
Python 2.7.x
Django 1.6

1,修改发信邮箱和接收通知邮箱：
simple-restful-proj/simple_rest_proj/settings.py 最下面几行，邮箱相关的服务器和端口等，修改为可用的即可。

2,初始化一个微型的 SQLite3数据库:
在控制台中执行:
simple-restful-proj/python manage.py syncdb

3,运行网站:
在控制台中执行:
simple-restful-proj/python manage.py runserver localhost:8000

4,在浏览器中访问如下url 就可以获得响应结果
http://localhost:8000/rest  (这里设计为可接受GET, POST请求)
http://localhost:8000/rest/[id]   (这里接受GET, PUT, DELETE请求)

Test
=============================
通过控制台输入以下，可以自动执行测试，
测试的目标是API 响应 正确的status 代码：
simple-restful-proj/python manage.py test
将会返回OK.

也可以在控制台中进入python shell再手动输入以下各行命令进行测试:
simple-restful-proj/python manage.py shell

>>> from django.test import Client
>>> import json
>>> c = Client()

>>> c.get('/rest').status_code
200

>>> data = {"email": "tester@test.com", "first_name": "Peter", "last_name": "Pan", "contact_number": "86-13227892789", "title": "Request Title", "content": "Request Content", "link": "https://github.com"}
>>> response = c.post('/rest', json.dumps(data), content_type="application/json")
<type 'dict'>
>>> response.status_code
201

>>> c.get('/rest/1').status_code
200

>>> response = c.put('/rest/1',json.dumps({"title":"new title"}), content_type="application/json")
<type 'dict'>
{u'title': u'new title'}
>>> response.status_code
200

>>> response = c.delete('/rest/1')
>>> response.status_code
200