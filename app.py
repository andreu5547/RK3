from flask import Flask
import csv

app = Flask(__name__)


def extract_students():
    with open('students.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def extract_students_dict():
    with open('students.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        return {inf['fio']: int(inf['id_task']) for inf in reader}


from routes import *

if __name__ == '__main__':
    app.run()
