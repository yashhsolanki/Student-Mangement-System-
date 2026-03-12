from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Student data store karne ke liye list
students = []

# Home Page
@app.get("/", response_class=HTMLResponse)
def home():

    html = """
    <h1>Student Management System</h1>
    <hr>

    <h2>Add Student</h2>
    <form action="/addstudent" method="post">
        Name: <input type="text" name="name"><br><br>
        Age: <input type="number" name="age"><br><br>
        <button type="submit">Add Student</button>
    </form>

    <br>

    <a href="/students">View Students</a>
    """

    return html


# Add Student
@app.post("/addstudent", response_class=HTMLResponse)
def add_student(name: str = Form(...), age: int = Form(...)):

    student = {
        "name": name,
        "age": age
    }

    students.append(student)

    return f"""
    <h2>Student Added Successfully</h2>
    <hr>
    <a href="/">Go Back</a>
    """


# View Students
@app.get("/students", response_class=HTMLResponse)
def view_students():

    html = "<h1>Student List</h1>"

    for i, student in enumerate(students):
        html += f"""
        <p>
        {student['name']} - {student['age']}
        <a href="/delete/{i}">Delete</a>
        </p>
        """

    html += '<br><a href="/">Home</a>'

    return html


# Delete Student
@app.get("/delete/{id}", response_class=HTMLResponse)
def delete_student(id: int):

    if id < len(students):
        students.pop(id)

    return """
    <h2>Student Deleted</h2>
    <a href="/students">Back</a>
    """