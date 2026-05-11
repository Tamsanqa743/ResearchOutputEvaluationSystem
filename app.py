from flask import Flask, render_template, url_for, request, flash
from BusinessLogic.submission_controller import submission_controller
import json
import os
import random

template_dir = os.path.abspath('Presentation/templates/') # custom template directory path
static_dir = os.path.abspath('Presentation/static/') # custom static directory path
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = 'DBHWGnxwhuxw802'

submission_controller = submission_controller()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit_research', methods=['POST'])
def submit_research():
    research_title = request.form.get("title")
    author = request.form.get("author")
    field_of_study = request.form.get("field-of-study")
    research_output = request.form.get("research-ouput")

    combined_submission = json.dumps({
        'research_title':research_title,
        'author': author,
        'field_of_study': field_of_study,
        'research_output': research_output
        })
    if submission_controller.validate_data_format((combined_submission)):
        operation_outcome = submission_controller.save_submission(combined_submission)
        print('Operation outcome:', operation_outcome)
        if operation_outcome:
            flash('Submission Successful!', "success")
        else: 
            flash("Error Sumbitting. Try Again", "danger")
    else:
        flash('Data Format Validation Failed', "danger")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)