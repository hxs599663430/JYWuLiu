from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from exts import db

from apps.user.models import User


# 获取模型中定义的类

app = create_app()
# Manager实例化对象
manage = Manager(app)

# 将app和db数据库绑定到迁移文库中
Migrate(app, db)
# 将迁移文件中用到的命令换成db开头(manage.py文件可以自行定义数据库命令)添加到manage中
manage.add_command("db", MigrateCommand)


# 在命令行中添加数据
@manage.option("-u", "--username", dest="username")
@manage.option("-p", "--password", dest="password")
@manage.option("-e", "--email", dest="email")
@manage.option("-tel", "--phone", dest="phone")
@manage.option("-pow", "--permission", dest="permission")
@manage.option("-emp", "--emp_no", dest="emp_no")
def add_user(*args, **kwargs):
    """
    用户添加: python manage.py add_user -u 用户名 -p 密码 -e 邮箱 -tel 手机号 -pow 权限值 -emp 员工编号
    :param args:
    :param kwargs: 命令行参数
    :return:
    """
    user = User(kwargs["username"], kwargs["password"], kwargs["email"],
                kwargs["phone"], kwargs["permission"], kwargs["emp_no"])
    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    manage.run()
