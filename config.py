import os

# 파일 복사, 디렉터리 생성, 특정 디렉터리 내의 파일 목록 구하기 등의 기능을 사용할 수 있는 os 모듈을 이용 해서
# __file__ : 현재 파이썬 스크립트의 파일 경로를 나타 내는 특수한 변수, 해당 스크립트 파일이 실행 중인 위치를 기준으로 현재 스크립트 파일의 절대 경로를 포함 한다.

# os.path.dirname() 함수를 이용해 현재 파이썬 스크립트의 전체 파일 경로에서 디렉토리 부분만 추출 해서 'BASE_DIR'에 담는다.
BASE_DIR = os.path.dirname(__file__)

# ORM 적용을 위해서 테이터 베이스 설정
# 데이터 베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLAlchemy 의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False
