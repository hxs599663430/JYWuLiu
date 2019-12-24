from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class Permission(object):
    """
    通过二进制的方式赋予7种权限，二进制的方式能更好的显示用户的叠加权限
    之后可以通过 &（与运算） 判断用户的权限、通过 |（或运算）赋予用户的权限
    """
    # 255的二进制方式来表示11111111
    # 1、超级管理员权限
    ALL_PERMISSION = 0b11111111
    # 2、访问者权限
    VISITOR = 0b00000001
    # 3、配送点管理员
    DEST_ADMIN = 0b00000010
    # 4、配送点操作员
    DEST_OPERATOR = 0b00000100
    # # 5、管理板块权限
    # BOARDER = 0b00001000
    # # 6、管理前台用户权限
    # FRONTUSER = 0b00010000
    # # 7、管理后台用户权限
    # CMSUSER = 0b00100000
    # # 8、后台管理员权限
    # ADMINER = 0b01000000


class User(db.Model):
    __tablename__ = "w_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True, comment="用户名称")
    _password = db.Column(db.String(100), nullable=False, comment="用户密码")
    email = db.Column(db.String(30), comment="用户邮箱")
    phone = db.Column(db.String(20), comment="用户手机号码")
    # 不使用权限表，给用户设置一个权限值
    permission = db.Column(db.Integer, default=Permission.VISITOR, comment="用户权限值")

    # 与配送点建立逻辑联系：配送点为1，用户为多
    # delivery_no = db.Column(db.String(30), db.ForeignKey("w_delivery.no"))

    # 与员工不建立物理联系，建立逻辑联系,关联关系员工编号
    emp_no = db.Column(db.String(30), unique=True, comment="员工编号")

    # delivery = db.relationship("DeliveryModel", backref="users")

    def __init__(self, username, password, email, phone, permission, emp_no):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.permission = permission
        self.emp_no = emp_no

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        res = check_password_hash(self._password, raw_password)
        return res

    def single_to_dict(self):
        """
        查询单个对象的处理
        :return: json格式数据
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def double_to_dict(self):
        """
        查询多个对象的处理
        :return: json格式数据
        """
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


def to_json(users):
    res = [user.double_to_dict() for user in users]
    params = {
        "code": 200,
        "data": res
    }
    return params
