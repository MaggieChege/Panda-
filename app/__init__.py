from flask import Flask,Blueprint


def create_app(config_name):
    app=Flask(__name__)
    from app.api.v2 import blue as v2
    app.register_blueprint(v2)
   
    



    return app
