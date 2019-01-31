# os模块进行文件操作和路径操作
import os, sqlite3
# dbfile = os.path.join(os.path.dirname(__file__), 'test.db')
# 连接到数据库文件
conn = sqlite3.connect('test.db')
# 创建一个游标
cursor = conn.cursor()
# 执行一句sql语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 执行一个sql语句，插入一条记录
cursor.execute('insert into user (id, name) values(\'1\', \'Michael\')')
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()