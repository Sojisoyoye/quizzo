# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.quiz import Quiz

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
quizzes= session.query(Quiz).all()

if len(quizzes) == 0:
    # create and persist dummy exam
    python_quiz = Quiz("SQLAlchemy Quiz", "Test your knowledge about SQLAlchemy.", "script")
    session.add(python_quiz)
    session.commit()
    session.close()

    # reload exams
    quizzes = session.query(Quiz).all()

# show existing exams
print('### Quizzes:')
for quiz in quizzes:
    print(f'({quiz.id}) {quiz.title} - {quiz.description}')