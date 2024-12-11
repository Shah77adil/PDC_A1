import pandas as pd
import time
import concurrent.futures


students_df = pd.read_csv('students_data.csv') 
fees_df = pd.read_csv('student_fees.csv')  


def process_data_parallel(students_df, fees_df):
    
    students_info = students_df[['Student ID', 'Student Name', 'Major']]
    payments_info = fees_df[['Student ID', 'Payment Date']]

   
    merged_data = pd.merge(students_info, payments_info, on='Student ID', how='inner')

    return merged_data


def process_in_parallel(students_df, fees_df):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(process_data_parallel, students_df, fees_df)
        return future.result()


start_time = time.time()
result_parallel = process_in_parallel(students_df, fees_df)
end_time = time.time()

execution_time_parallel = end_time - start_time
print(f"Processed Data (Parallel):\n{result_parallel.head()}")
print(f"Execution Time (Parallel): {execution_time_parallel:.4f} seconds")
