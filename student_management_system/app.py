from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# DATABASE CREATION
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_no TEXT NOT NULL,
        department TEXT,
        marks INTEGER
    )
    ''')

    conn.commit()
    conn.close()

# HOME PAGE
@app.route('/')
def index():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)

# ADD STUDENT
@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    roll_no = request.form['roll_no']
    department = request.form['department']
    marks = request.form['marks']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students(name, roll_no, department, marks)
    VALUES (?, ?, ?, ?)
    """, (name, roll_no, department, marks))

    conn.commit()
    conn.close()

    return redirect('/')

# DELETE STUDENT
@app.route('/delete/<int:id>')
def delete_student(id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
