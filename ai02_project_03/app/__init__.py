from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

#from models.weather_model import Weather



migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')
    


    from app.routes import main_route, predict_route

    app.register_blueprint(main_route.bp)
    app.register_blueprint(predict_route.bp)

# @bp.route('/user')
# def user_index():
#     """
#     user_list 에 유저들을 담아 템플렛 파일에 넘겨주세요
#     """

#     msg_code = request.args.get('msg_code', None)
    
#     #alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

#     user_list = weather_model.User.query.all()

#     return render_template('user.html',
#      #alert_msg=alert_msg,
#         user_list=user_list)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

    