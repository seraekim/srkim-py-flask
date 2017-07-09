from flask import Flask, render_template, make_response
from config import Config
from apps.main import models

app = Flask(__name__)
conf = Config(app)
log = conf.get_logger()
models.set_engine(conf.get_db_engine())


@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')


@app.route('/read', methods=['GET', 'POST'])
def read():
    res = models.read()
    return make_response(res, 200, {'Content-Type': 'application/json; charset=utf-8'})


# @app.before_request
# def before_request():
#     g.db = conf.get_db()
#
#
# @app.teardown_request
# def teardown_request(e):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()



app.run(use_reloader=True)
