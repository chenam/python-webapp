# 导入MYSQL驱动
import mysql.connector
# 建立连接
conn = mysql.connector.connect(user = 'root', password='password', database='test')
# 创建游标
cursor = conn.cursor()
# 创建 user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
# 关闭Cursor和Connection:
cursor.close()
conn.close()
