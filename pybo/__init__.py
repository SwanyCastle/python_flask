from flask import Flask
# SQLAlchemy 를 사용하는 Flask 애플리케이션에서 데이터 베이스 스키마를 쉽게 관리 할 수 있도록 도와 주는 친구
# 데이터 베이스를 사용하다보면 스키마(구조)를 변경해야 하는 경우가 종종 있는데 그 때 마이그레이션 스크림트를 생성하고 적용하는 명령을 제공한다.
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


# 애플맄케이션 팩토링
def create_app():
    # 플라스크 객체로 app 생성
    app = Flask(__name__)
    # config.py 파일에 작성한 항목들 읽기
    app.config.from_object(config)

    # ORM
    # SQLAlchemy 의 init_app 메서드를 호출하여 데이터 베이스 객체를 Flask 애플리케이션에 연결
    db.init_app(app)
    # 마이그레이션을 초기화 하기 위해 Flask 애플리케이션과 SQLAlchemy 데이터 베이스를 연결
    migrate.init_app(app, db)

    # pybo 폴더 안에 있는 views 폴더에 main_views.py을 임포트
    from .views import main_views
    # 블루프린트로 등록 (다른 views 파일들도 마찬가지)
    app.register_blueprint(main_views.bp)

    return app
