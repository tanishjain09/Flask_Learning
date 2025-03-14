from flask import render_template,request

from models import User

def register_router(app,db):

    @app.route('/',methods =['GET','POST'])
    def index():
        return ""