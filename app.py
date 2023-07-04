import sqlite3

from flask import Flask,request,jsonify
app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('students.sqlite')
    except sqlite3.error as e:
        print(e)

    return  conn
@app.route('/')
def hello():
    return  "Hello There "

@app.route('/students',methods=['GET','POST'])
def stud():
    conn= db_connection()
    curr = conn.cursor()

    if request.method == 'GET':
        curr = conn.execute("Select * from student")
        student = [dict(id=row[0] , name=row[1],branch=row[2])
                   for row in curr.fetchall()
                   ]
        if student is not None:
            return jsonify(student)


    if request.method == 'POST':

        new_name1 = request.get_json()
        new_name = new_name1['name']
        new_br1 = request.get_json()
        new_br = new_br1['branch']

        sql = """Insert into student (name , branch ) VALUES (? , ? )"""

        cursor = curr.execute(sql,(new_name , new_br))
        conn.commit()


        return f"Book With ID : {cursor.lastrowid} created successful",201

@app.route('/students/<int:id>',methods=['GET','PUT','DELETE'])
def single(id):
    conn = db_connection()
    curr = conn.cursor()
    student = None

    if request.method =='GET':
        curr.execute("Select * from student where id = ?", (id,))

        row = curr.fetchall()
        #for i in row:
        student =  [dict(id=i[0] , name=i[1],branch=i[2]) for i in row ]
        if student:
            return jsonify(student),201
        else:
            return "Something Wrong" , 401

    if request.method == 'PUT':
        sql = """Update student SET name = ?,branch = ? Where id = ? """

        branch = request.form['branch']
        name = request.form['name']


        updated = {
            'id' : id,
            'name': name ,
            'branch' : branch

            }
        conn.execute(sql,(name,branch,id))
        conn.commit()
        return jsonify({'updated':updated})



    if request.method =='DELETE':
        sql = """Delete from student where id = ?"""

        #conn = db_connection()
        #curr = conn.cursor()
        conn.execute(sql,(id,))
        conn.commit()
        return  "The book with id : {} has deleted ".format(id)



if __name__ == "__main__":
    app.run(debug=True)
