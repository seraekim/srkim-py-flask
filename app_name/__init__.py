# root routes
from flask import Flask, redirect
from app_name.routes.task01.sub01 import t01_s01
from app_name.routes.task02 import mongo
from app_name.util import DB

app = Flask(__name__)

DB(app)

app.register_blueprint(t01_s01, url_prefix='/t01/s01')
app.register_blueprint(mongo, url_prefix='/t02')


@app.route('/')
def root_redir():
    return redirect('t01/s01')

