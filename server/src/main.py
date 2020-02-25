# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from entities.entity import Session, engine, Base
from entities.quiz import Quiz, QuizSchema


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


if __name__ == '__main__':
    app.run()




