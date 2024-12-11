import pandas as pd
import time
import concurrent.futures

# Step 1: Read Data (Assuming both CSVs exist and have required columns)
students_df = pd.read_csv('students_data.csv')  # Columns: ['student_id', 'name', 'major', ...]
fees_df = pd.read_csv('student_fees.csv')  # Columns: ['student_id', 'payment_date', 'amount', ...]

# Step 2: Extract Relevant Data (Parallel Execution)
def process_data_parallel(students_df, fees_df):
    # Extract required columns
    students_info = students_df[['Student ID', 'Student Name', 'Major']]
    payments_info = fees_df[['Student ID', 'Payment Date']]

    # Merge the datasets on student_id
    merged_data = pd.merge(students_info, payments_info, on='Student ID', how='inner')

    return merged_data

# Step 3: Multi-threading Approach (Parallel Execution)
def process_in_parallel(students_df, fees_df):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(process_data_parallel, students_df, fees_df)
        return future.result()

# Step 4: Measure Execution Time (Parallel Execution)
start_time = time.time()
result_parallel = process_in_parallel(students_df, fees_df)
end_time = time.time()

execution_time_parallel = end_time - start_time
print(f"Processed Data (Parallel):\n{result_parallel.head()}")
print(f"Execution Time (Parallel): {execution_time_parallel:.4f} seconds")
