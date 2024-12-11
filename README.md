# PDC_A1
Student Fee Data Analysis: Serial vs Parallel Programming.
PDC Assignment: Parallel and Serial Programming
Name: Shaheer Adil
Roll No: 21B-095-CS

Overview:
This project contains implementations of both serial and parallel programming techniques to process and analyze large student fee datasets. The goal is to efficiently extract relevant data from the given CSV files and compare the performance of serial vs parallel approaches in processing such large datasets.

The project demonstrates:
Serial Programming:
A straightforward approach to process data sequentially.
Extracts student ID, name, and payment date for each fee record and calculates the most consistent payment date.
Parallel Programming:
Utilizes Python’s multiprocessing library to split data into chunks and process them in parallel.
Extracts student ID, name, and payment date for each fee record, with significantly improved execution time when handling large datasets.
Files in the Project
serial_programming.py

Implements the serial approach for processing the student fee data and calculating the most consistent payment dates.
parallel_programming.py

Implements the parallel approach using multiprocessing to improve performance and handle larger datasets more efficiently.
students_data.csv

Contains student details, including student IDs, names, and other relevant information.
student_fees.csv

Contains fee payment records, including payment dates for each student.
Technologies Used
Python: Programming language used for implementing both serial and parallel approaches.
Pandas Library: Used for data manipulation and analysis of the CSV files.
Multiprocessing Library: Enables parallel processing to reduce execution time when processing large datasets.
Key Features
Efficiently calculates the most consistent payment date for each student.
Comparison of serial vs parallel processing speeds and performance on a large dataset.
Shows the execution time difference between serial and parallel approaches.
Usage
Ensure that the required files (students_data.csv and student_fees.csv) are present in the project directory.

To analyze the data, run either of the following Python scripts:

For Serial Approach:

bash

python serial.py
For Parallel Approach:

bash

python parallel.py
