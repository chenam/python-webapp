import asyncio, logging
from orm import Model, StringField, IntegerField
# IntegerField整型

# 创建连接池
@asyncio.coroutine
# 命名关键字参数，函数的调用者可以传入任意不受限制的关键字参数，函数内部通过kw检查 => dict
# dect.get()
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port','3306'),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset','utf8'),
        autocommit = kw.get('autocommit', true),
        maxsize = kw.get('maxsize', 10),
        minsize = kw.get('minsize', 1),
        loop = loop
    )

# 在函数内定义全局作用域，需要加上global修饰符

# 执行SELECT语句
@asyncio.coroutine
def select(sql, args, size = None):
    log(sql, args)
    global __pool
    # with 可以先设置，后进行清理工作，并且可以处理异常
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.excute('?','%s', args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else: 
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

# 执行INSERT、UPDATE、DELETE，定义一个通用的execute()函数
@asyncio.coroutine
def excute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from  conn.cursor()
            yield from cur.excute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
            # BaseException所有异常的基类
        except BaseException as e:
            raise
        return affected

# 先定义一个User对象，然后把数据库表users和它关联起来
class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key = True)
    name = StringField()

user = User(id=123, name='amy')
user.insert()
users = User.findall()
logging.info('users', users)
