# coding=utf-8


from flask import Flask, jsonify, request


from .entities.entity import Session, engine, Base
from .entities.quiz import Quiz, QuizSchema

app = Flask(__name__)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/quizzes')
def get_quizzes():
    # fetching from the database
    session = Session()
    quiz_objects = session.query(Quiz).all()

    # transforming into JSON-serializable objects
    schema = QuizSchema(many=True)
    quizzes = schema.dump(quiz_objects)

    print(f'"WWWWW:" {quizzes}')

    # serializing as JSON
    session.close()
    return jsonify(quizzes)



@app.route('/quizzes', methods=['POST'])
def add_quiz():
    # mount quiz object
    posted_quiz = QuizSchema(only=('title', 'description'))\
        .load(request.get_json())

    quiz = Quiz(**posted_quiz.data, created_by="HTTP post request")

    # persist quiz
    session = Session()
    session.add(quiz)
    session.commit()

    # return created quiz
    new_quiz = QuizSchema().dump(quiz).data
    session.close()
    return jsonify(new_quiz), 201
    