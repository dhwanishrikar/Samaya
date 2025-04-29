from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/processing')
def processing_page():
    return render_template('processing.html')

@app.route('/generate-timetable', methods=['POST'])
def generate_timetable():
    # Initialize lists to hold all the entries
    teacher_names = request.form.getlist('teacherNames')
    subjects = request.form.getlist('subjects')
    classrooms = request.form.getlist('classrooms')
    times = request.form.getlist('times')
    capacities = request.form.getlist('capacities')

    timetable = []
    
    # For each set of entries, create a timetable entry
    for teacher, subject, classroom, time, capacity in zip(teacher_names, subjects, classrooms, times, capacities):
        entry = {
            'teacher': teacher.strip(),
            'subject': subject.strip(),
            'classroom': classroom.strip(),
            'time': time.strip(),
            'capacity': capacity.strip()
        }
        timetable.append(entry)

    return render_template('timetable.html', timetable=timetable)

@app.route('/timetable')
def timetable_page():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True)
