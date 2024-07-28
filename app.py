from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Firebase Admin SDK
cred = credentials.Certificate('p2030-93e55-firebase-adminsdk-8qbf3-4f0e14f097.json')
firebase_admin.initialize_app(cred)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.get_user_by_email(email)
            # Here you should validate the password (this is an example, adapt as needed)
            # Since Firebase Admin SDK does not support password authentication directly,
            # you may need to handle this via the Firebase client-side SDK or other method
            session['user_id'] = user.uid
            return redirect(url_for('student_home'))
        except Exception as e:
            return str(e), 401
    return render_template('student-login.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.get_user_by_email(email)
            # Validate the password similarly as noted above
            session['user_id'] = user.uid
            return redirect(url_for('admin_home'))
        except Exception as e:
            return str(e), 401
    return render_template('admin-login.html')

@app.route('/student-home')
def student_home():
    if 'user_id' in session:
        return render_template('student-home.html')
    return redirect(url_for('student_login'))

@app.route('/admin-home')
def admin_home():
    if 'user_id' in session:
        return render_template('admin-home.html')
    return redirect(url_for('admin_login'))

if __name__ == "__main__":
    app.run(debug=True)
