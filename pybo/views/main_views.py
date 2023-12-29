from flask import Blueprint

# 블로프린트(Blue Print) : URL 과 함수의 매핑을 관리하기 위해 사용 되는 도구
bp = Blueprint('main', __name__, url_prefix='/')


# route 애너테이션으로 '/' 경로의 url 이 들어오면 아래의 내용을 실행
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo Index!'
