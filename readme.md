# 监控项目手记
##1. 虚拟独立开发环境

	virtualenv --no-site-packages [虚拟环境名称]

##2. python3连接mysql需要在Init.py汇总配置

装好pymysql即可
	import pymysql
	pymysql.install_as_MySQLdb()

##3 django2中设置外键

	system = models.ForeignKey(System,on_delete=models.CASCADE)
on_delete参数必须要写出

##4 前提是建库
	
然后缓存
	python manage.py makemigrations

真正建表

	python manage.py migrate

##5 数据库整型数据需要加default

	models.IntegerField(default=0)
##6 django的MVC理解

	models：数据库模型，类名为表，属性为字段，实例对象为数据
	urls:浏览器访问路径Url设置
	views:执行的操作