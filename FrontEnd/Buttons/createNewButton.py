import pandas as pd
import os

def save_project_to_csv(project_data):
    csv_file_path = os.path.join(os.path.dirname(__file__), '../../BackEnd/csv/newProject.csv')
    
    # Create a DataFrame from the project data
    df = pd.DataFrame([project_data])
    
    # Debug: Print the DataFrame and file path
    print(f"Attempting to save data to: {csv_file_path}")
    print(f"Data to save: {df}")

    if os.path.exists(csv_file_path):
        try:
            existing_df = pd.read_csv(csv_file_path)
            df.to_csv(csv_file_path, mode='a', header=False, index=False)
            print(f"Data appended to existing file.")
        except pd.errors.EmptyDataError:
            # File is empty, write header
            df.to_csv(csv_file_path, mode='w', header=True, index=False)
            print(f"New file created and data written.")
    else:
        # File doesn't exist, create it with header
        df.to_csv(csv_file_path, mode='w', header=True, index=False)
        print(f"New file created and data written.")
