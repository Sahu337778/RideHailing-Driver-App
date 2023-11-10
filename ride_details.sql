CREATE database ride_details;
use ride_details;
CREATE TABLE IF NOT EXISTS accepted_rides (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            destination VARCHAR(255),
                            passenger_name VARCHAR(255),
                            status VARCHAR(50));
SELECT * FROM accepted_rides;
DROP TABLE accepted_rides;
CREATE TABLE IF NOT EXISTS accepted_rides (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            pickup_location VARCHAR(255),
                            destination VARCHAR(255),
                            passenger_name VARCHAR(255),
                            status VARCHAR(50));

