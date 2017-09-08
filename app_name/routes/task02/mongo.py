from flask import Blueprint, render_template as rt, make_response as ms, request as req
from app_name.util import DB
from pandas import DataFrame

mongo = Blueprint('mongo', __name__)


@mongo.route('/')
def mngo_root():
    series = list(DB.mongo.db.series.find())
    for doc in series:
        print(doc)
    
    df = DataFrame(series).to_html()
    print(df)
    return rt('t2/t02_temp.html', df=df)