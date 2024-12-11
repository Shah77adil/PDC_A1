import pandas as pd
import time

# Step 1: Read Data (Assuming both CSVs exist and have required columns)
students_df = pd.read_csv('students_data.csv')  # Columns: ['student_id', 'name', 'major', ...]
fees_df = pd.read_csv('student_fees.csv')  # Columns: ['student_id', 'payment_date', 'amount', ...]

# Step 2: Extract Relevant Data
def process_data_serial(students_df, fees_df):
    # Extract required columns
    students_info = students_df[['Student ID', 'Student Name', 'Major']]
    payments_info = fees_df[['Student ID', 'Payment Date']]

    # Merge the datasets on student_id
    merged_data = pd.merge(students_info, payments_info, on='Student ID', how='inner')

    return merged_data

# Step 3: Measure Execution Time (Serial Execution)
start_time = time.time()
result_serial = process_data_serial(students_df, fees_df)
end_time = time.time()

execution_time_serial = end_time - start_time
print(f"Processed Data (Serial):\n{result_serial.head()}")
print(f"Execution Time (Serial): {execution_time_serial:.4f} seconds")
