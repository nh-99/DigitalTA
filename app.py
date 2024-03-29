# 3rd Party Imports
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os, uuid, subprocess

# Local imports
import models
from models import Assignment, HomeworkCheck
from config import config

app = Flask(__name__)
app.config.from_object(config['dev'])

models.db.init_app(app)


# Index page
@app.route('/')
def index():
    return render_template('index.html')


# File upload route
@app.route('/upload', methods=['POST'])
def homework_upload():
    # Save the file
    file = request.files['homework']
    file2 = request.files['homeworksrc']
    filename = str(uuid.uuid4())
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename + '.jar')))
    file2.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename + '.zip')))

    # Add file to the database of assignments
    assignment = Assignment(id=filename, name=file.filename)
    models.db.session.add(assignment)
    models.db.session.commit()

    return redirect('/')


@app.route('/check', methods=['GET'])
def create_check():
    check = HomeworkCheck(stdin=request.args.get('stdin'))
    models.db.session.add(check)
    models.db.session.commit()
    return redirect('/')


@app.route('/check/<string:id>')
def check_homework(id):
    check_id = request.args.get('check')
    check = HomeworkCheck.query.filter_by(id=check_id).first()
    assignment = Assignment.query.filter_by(id=id).first()

    # Check the homework against the check
    bash_cmd = 'echo "{}" | java -jar {}'.format(check.stdin, 'uploads/' + assignment.id + '.jar')
    output = os.popen(bash_cmd).read()

    # Save the output to the assignment
    assignment.output = output
    models.db.session.add(assignment)
    models.db.session.commit()

    return redirect('/grade/' + assignment.id)


@app.route('/grade/<string:id>')
def grade_homework(id):
    assignment = Assignment.query.filter_by(id=id).first()

    return render_template('grade.html', assignment=assignment)


@app.route('/grade/finish', methods=['POST'])
def finish_grading():
    id = request.form.get('id')
    points = request.form.get('points')

    assignment = Assignment.query.filter_by(id=id).first()
    assignment.graded = True
    assignment.score = float(points)

    models.db.session.add(assignment)
    models.db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    models.db.create_all()
    app.run(host='0.0.0.0', port=5000)
