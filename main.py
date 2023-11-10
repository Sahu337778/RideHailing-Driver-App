from flask import Flask, render_template, request, redirect, url_for
import pymysql
import hashlib

app = Flask(__name__)

class RideHailingDriverApp:
    def __init__(self):
        self.db_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Root@1234",
            database="ride_details"
        )
        self.cursor = self.db_connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS drivers (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            email VARCHAR(255) UNIQUE,
                            password VARCHAR(255))''')
        self.db_connection.commit()

    def driver_login(self, email, password):
        hashed_password = self.hash_password(password)
        self.cursor.execute("SELECT * FROM drivers WHERE email=%s AND password=%s",
                            (email, hashed_password))
        return bool(self.cursor.fetchone())

    def driver_signup(self, email, password):
        if self.validate_signup(email, password):
            hashed_password = self.hash_password(password)
            self.cursor.execute("INSERT INTO drivers (email, password) VALUES (%s, %s)",
                                (email, hashed_password))
            self.db_connection.commit()
            return True
        else:
            return False

    def validate_signup(self, email, password):
        # Validate email format
        if '@' not in email or '.' not in email:
            return False

        # Validate password length
        if len(password) < 8:
            return False

        return True

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def store_accepted_ride(self, destination, passenger_name):
        self.cursor.execute("INSERT INTO accepted_rides (destination, passenger_name, status) VALUES (%s, %s, %s)",
                            (destination, passenger_name, "Accepted"))
        self.db_connection.commit()

    def list_accepted_rides(self):
        self.cursor.execute("SELECT * FROM accepted_rides WHERE status='Accepted'")
        return self.cursor.fetchall()

# Instantiate the RideHailingDriverApp
app_instance = RideHailingDriverApp()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if app_instance.driver_login(email, password):
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/signup', methods=['POST'])
def signup():
    new_email = request.form['new_email']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    if new_password == confirm_password:
        if app_instance.driver_signup(new_email, new_password):
            return "Account created successfully! You can now login."
        else:
            return "Email already exists or invalid email/password format. Please check and try again."
    else:
        return "Passwords do not match. Please try again."

@app.route('/dashboard')
def dashboard():
    accepted_rides = app_instance.list_accepted_rides()  # Fetch accepted rides
    return render_template('dashboard.html', accepted_rides=accepted_rides)

@app.route('/accept-ride', methods=['POST'])
def accept_ride():
    destination = request.form['destination']
    passenger_name = request.form['passenger_name']

    app_instance.store_accepted_ride(destination, passenger_name)
    # Simulated ride ID, replace this with your logic to get the actual ride ID
    ride_id = 1

    return render_template('otp.html', ride_id=ride_id)

@app.route('/process-otp', methods=['POST'])
def process_otp():
    otp = request.form['otp']
    ride_id = request.form['ride_id']

    if otp == '9999':
        return f"Success! OTP verified for ride ID: {ride_id}. Go ahead!"
    else:
        return "Invalid OTP. Ride not accepted."

if __name__ == '__main__':
    app.run(debug=True)

