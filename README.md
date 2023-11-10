# RideHailing Driver App

This is a simple RideHailing Driver App built using Flask and MySQL.

## Features

- **User Authentication:** Allows drivers to sign up and log in securely.
- **Dashboard:** Displays a dashboard with accepted ride details.
- **Accept Ride:** Drivers can accept a ride, and an OTP verification is implemented.

## Requirements

- Python 3.x
- Flask
- MySQL

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sahu337778/ridehailing-driver-app.git
    cd ridehailing-driver-app
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the MySQL database:**
   - Create a MySQL database named `ride_details`.
   - Update the `pymysql.connect` parameters in the `RideHailingDriverApp` class with your MySQL credentials.

4. **Run the application:**

    ```bash
    python app.py
    ```

   Access the application at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open your browser and go to [http://localhost:5000](http://localhost:5000).
2. Sign up or log in as a driver.
3. Explore the dashboard, accept rides, and verify OTP for accepted rides.

## Contributing

Contributions are welcome! If you have suggestions or find any issues, please open an [issue](https://github.com/your-username/ridehailing-driver-app/issues) or create a pull request.



