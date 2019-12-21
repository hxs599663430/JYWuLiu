from flask import Flask
import config
from exts import db, swagger, api, mail

from apps.user import user_bp


def create_app():
    # app初始化
    app = Flask(__name__)
    # 导入配置文件
    app.config.from_object(config)

    # 第三方库的实例注册到app中
    db.init_app(app)
    swagger.init_app(app)
    api.init_app(app)
    mail.init_app(app)

    # 蓝图注册
    app.register_blueprint(user_bp, url_prefix="/user")

    return app


if __name__ == "__main__":
    start = create_app()
    start.run()
