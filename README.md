
#### Quizzo

An online quiz/exam app built with Python, Flask, and Angular.

## To start the app without bootstrap.sh file

**Cd into server**

> Run `pipenv shell`
> Run `export FLASK_APP=./src/main.py`
> Run `export FLASK_ENV=development # enables debug mode`
> Run `python3 main.py `

## To test the routes

> Run `curl http://127.0.0.1:5000/quiz` for GET
> Run `curl -X POST -H 'Content-Type: application/json' -d '{"title": "TypeScript Advanced Exam", "description": "Tricky questions about TypeScript."}' http://0.0.0.0:5000/quiz` for POST


More details to come ......