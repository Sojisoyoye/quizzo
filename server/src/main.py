# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from entities.entity import Session, engine, Base
from entities.quiz import Quiz, QuizSchema
from auth import AuthError, requires_auth

app = Flask(__name__)
CORS(app)


# generate database schema
Base.metadata.create_all(engine)


@app.route('/quiz')
def get_quiz():
    # fetching from the database
    session = Session()
    exam_objects = session.query(Quiz).all()

    # transforming into JSON-serializable objects
    schema = QuizSchema(many=True)
    quiz = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(quiz)


@app.route('/quiz', methods=['POST'])
@requires_auth
def add_exam():
    # mount exam object
    posted_quiz = QuizSchema(only=('title', 'description'))\
        .load(request.get_json())

    quiz = Quiz(**posted_quiz, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(quiz)
    session.commit()

    # return created exam
    new_quiz = QuizSchema().dump(quiz)
    session.close()
    return jsonify(new_quiz), 201


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


if __name__ == '__main__':
    app.run()




