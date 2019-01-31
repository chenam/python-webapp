# 定义所有ORM映射的基类 Model

# type类是所有类的元类
# metaclass 元类 可以动态修改类

# 对于你定义的每一个类，python 会计算出一个方法解析顺序（Method Resolution Order）,它代表了类继承的顺序

# 1. 子类永远在父类前面
# 2. 如果有多个父类， 会根据他们在列表中的顺序被检查
# 3. 如果对下一个类存在两个合法的选择，选择第一个父类
 
class Model(dict, metaclass = ModelMetaclass):

    def __init__(self, **kw):
        # 调用父类的方法
        # 使用多继承，会有查找顺序（mro）
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try: 
            return self[key]
        except KeyError:
            # 特征引用或者赋值失败时引发的
            raise AttributeError(r"'Modal' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings.items():

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    
    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.name)
    

class StringField(Field):
    def __init__(self, name):
        super (StringField, self).__init__(name, 'varchar(100)')
