from flask import Flask, render_template, request, redirect, url_for, flash
from models import Member, Attendance, db  # Import your models and database
from database_setup import init_db, db_session
from database_setup import get_members_data
from util import check_admin_status



app = Flask(__name__)
app.config['SECRET_KEY'] = 'repent'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data and create a new member
        new_member = Member(
            name=request.form['name'],
            encoding='sample_encoding',  # Replace with actual encoding
            phone_number=request.form['phone_number'],
            residence=request.form['residence'],
            age=request.form['age'],
            home_fellowship=request.form['home_fellowship'],
            department=request.form['department']
        )
        db.session.add(new_member)
        db.session.commit()
        flash('Member registered successfully!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html')

from flask import render_template, request

@app.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        department = request.form.get('department')
        
        # Fetch attendance data from the database based on the criteria
        # Replace this with your actual database query logic
        
        attendance_data = [
            {'name': 'John', 'date': '2023-08-01', 'status': 'Present'},
            {'name': 'Jane', 'date': '2023-08-01', 'status': 'Absent'},
            # ... more data
        ]
        
        return render_template('attendance_report.html', attendance_data=attendance_data)
    
    return render_template('generate_report.html')


# Implement similar routes and views for marking attendance and viewing reports

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Member, Attendance

from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'repent'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'

# Initialize the database
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

# Define your Flask routes and views here

# ... (previous imports and code)

from flask import Flask, render_template, request, redirect, url_for, flash
# ... (other imports)

@app.route('/mark_attendance', methods=['GET', 'POST'])
def mark_attendance():
    if request.method == 'POST':
        face_id = request.form.get('face_id')

        if face_id:
            member = db_session.query(Member).filter_by(encoding=face_id).first()
            if member:
                new_attendance = Attendance(member=member, marked_time=str(datetime.now()))
                db_session.add(new_attendance)
                db_session.commit()
                flash(f"Attendance marked for {member.name}")
                return redirect(url_for('mark_attendance'))
            else:
                flash("Member not found")
        else:
            flash("Please provide a valid face ID")

    return render_template('mark_attendance.html')

# ... (other routes and the if __name__ == '__main__': block)

from flask import render_template

# ... (other imports and code)

@app.route('/view_reports')
def view_reports():
    # Fetch attendance records from the database
    attendances = db_session.query(Attendance).order_by(Attendance.marked_time.desc()).all()
    return render_template('view_reports.html', attendances=attendances)

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for mark attendance page
@app.route('/mark_attendance', methods=['GET'])
def mark_attendance():
    return render_template('mark_attendance.html')

# API endpoint for marking attendance
@app.route('/api/mark_attendance', methods=['POST'])
def api_mark_attendance():
    data = request.json  # Get JSON data from the POST request
    face_id = data.get('face_id')  # Extract the recognized face ID
    # Perform attendance marking logic (e.g., update the database)
    # Return a response indicating success or failure
    return jsonify(message='Attendance marked for face ID: ' + face_id)

def members():
    # Fetch member data from the database
    members = get_members_data()

    # Get admin status (you'll need to implement this)
    is_admin = check_admin_status()

    return render_template('members.html', members=members, is_admin=is_admin)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'G45main' and password == 'repent':
        return redirect(url_for('admin'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/admin')
def admin():
    return "Welcome to the admin page!"

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
