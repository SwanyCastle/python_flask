# __init__.py 파일에서 생성한 SQLAlchemy 클래스의 객체인 db를 임포트
from pybo import db


# SQLAlchemy 클래스의 객체인 db의 db.Model 상속받아 만듬
class Question(db.Model):
    # 아이디는 고유한 값으로 프라이머리키로 지정함
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 답변은 어떤 질문에 대한 답변인지 구분하기 위해서 질문과 연결되어 있어야 하기에 질문의 id가 필요
    # 외부키로 질문 테이블의 id 값을 참조하고, ondelete=CASCADE 는 질문이 삭제되면 외부키도 같이 삭제 된다는 의미
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # question 속성은 답변 모델에서 질문 모델을 참조 하기 위해서 추가 했고
    # 답변 모델에서 질문 모델의 제목을 (answer.question.subject) <- 이런식으로 접근 가능
    # relationship() 메서드의 첫 파리미터는 참조할 모델의 이름이고, backref 는 역참조이다 역참조는 질문에서 답변을 역으로 참조하는 것을 의미
    question = db.relationship('Question', backref=db.backref('answer_set'))
