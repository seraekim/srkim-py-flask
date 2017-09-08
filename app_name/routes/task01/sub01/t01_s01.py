from flask import Blueprint, render_template as rt, make_response as ms, request as req
from app_name.util import DB, to_json
import json, socket

t01_s01 = Blueprint('t01_s01', __name__)


@t01_s01.route('/')
def t01_s01():
    var = '나의 변수 넘기기.. jinja 템플릿에서 인식 함'
    kwargs = {'hi': 'hi', 'yes': 'yes'}
    return rt('t01/t01.html', var=var, **kwargs)


@t01_s01.route('/t01/s01/any/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def methods_t01_s01_any__id(id):
    kwargs = {}
    # path variable
    print(id)

    # request 요청 데이터
    hello = req.values.get('hello')

    # dynamic json request(dict/list) 가져오기
    # 위험한 방법 all = json.loads(list(req.values.to_dict().keys())[0])
    # = 가 :로 변경되어 flask에서 처리. to_dict().keys()가 :에서 짤리는 등 char xxx 하면서 디코드 에러
    # ajax data : {key: JSON.stringify(params)}
    all = json.loads(req.values.get('key'))


    sql = """
    select * from .... '{}', '{ok}'
    """.format(hello, ok='No', **kwargs).replace("'None'", 'null')

    # string이 아닌 list/dict로 되게 하려면 is_str 을 False로
    res = to_json(DB.exec(sql))

    # insert, update, delete 등은 rowcount로 확인 가능
    cnt = DB.exec(sql).rowcount

    # select 값 하나만을 가져올 때
    select_one_cell = to_json(DB.exec(sql), is_str=False)[0].get('column_name')


    # 다른 헤더 등을 추가하고 싶다면 여러 방법이 있긴한데.. 그나마 간단한건..
    res = ms(res)
    res.headers['Content-Type'] = 'application/json; charset=utf-8'

    # dict를 만들어 json으로 응답하기..
    res = json.dumps({'state': 'OK'})
    return res


@t01_s01.route('/test01/<id>')
def test01(id):
    s = socket.socket()
    s.connect(('localhost',12345))
    s.sned(str(id).encode())
    s.close()
    return json.dumps({'good':'good'})

