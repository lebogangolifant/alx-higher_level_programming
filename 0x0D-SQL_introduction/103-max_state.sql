-- Import the provided table dump into hbtn_0c_0 database
USE hbtn_0c_0c_0

SELECT state, MAX(temperature_fahrenheit) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
