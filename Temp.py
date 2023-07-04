'''from flask import Flask
from flask import requestz
app = Flask(__name__)

@app.route('/')
def param():
    return "Rajat Here"

@app.route('/<name>')
def print_name(name):
    return "Welcome, {}".format(name)



if __name__== "__main__":
    app.run(debug=True)

import sqlite3

from flask import Flask,request,jsonify
app = Flask(__name__)

#students = [
    {
        "id" : 1,
        "name" : "Rajat Lalzare",
        "branch" : "IT"

    },
{
        "id" : 2,
        "name" : "Ayush Paunikar",
        "branch" : "IT"

    },
{
        "id" : 3,
        "name" : "Pankaj Raut",
        "branch" : "IT"

    },
{
        "id" : 4,
        "name" : "Nikhil Surkar",
        "branch" : "CSE"

    },
{
        "id" : 5,
        "name" : "Gunjan Tambekar",
        "branch" : "AI"

    }
]
'''
'''
def db_connection():
    conn = None 
    try:
        conn = sqlite3.connect('students.sqlite') 
    except sqlite3.error as e:
        print(e) 
        
    return  conn
        

@app.route('/students',methods=['GET','POST'])
def stud():
    conn= db_connection() 
    curr = conn.cursor()

    if request.method == 'GET':
        if len(students) > 0:
            return jsonify({'retrieved':students})
        else:
             "Error"

    if request.method == 'POST':
        new_name = request.form['name']
        new_br = request.form['branch']

        ids = students[-1]['id']+1

        new_obj = {
            "id": ids,
            "name": new_name,
            "branch": new_br

        }
        students.append(new_obj)

        return jsonify({'message':students}),201

@app.route('/students/<int:id>',methods=['GET','PUT','DELETE'])
def single(id):
    if request.method =='GET':
        for i in students:
            if i['id'] == id:
                return jsonify({'fetched':i})


            pass
    if request.method == 'PUT':
        for j in students:
            if j['id'] == id:
                j['branch'] = request.form['branch']
                j['name'] = request.form['name']


                updated = {
                    'id' : id,
                    'name': j['name'] ,
                    'branch' : j['branch']

                }

                return jsonify({'updated':updated})



    if request.method =='DELETE':
        for i,j in enumerate(students):
            if j['id'] == id:
                students.pop(i)
                return jsonify({'removed':students})


if __name__ == "__main__":
    app.run(debug=True)
'''