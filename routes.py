from app import app, extract_students
from flask import render_template, request



@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        fio = request.form['student']
        #if (id_task := get_students_dict()[fio]) == -1:
        #    task = set_id_task(fio)
        #else:
        #    task = get_tasks()[id_task]

        return render_template('form.html', students=extract_students())#, task=task)

    return render_template('form.html', students=extract_students())