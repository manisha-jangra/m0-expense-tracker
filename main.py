import sys
import os
from db import insert_csv_records
from csv_reader import read_csv_file
from analytics import run_analytics

def main():
    # check if argument is passed
    if len(sys.argv) > 1 and sys.argv[1] == "ingest":
        
        print("Running CSV ingestion...")
        folder_path = "data"
        
        list_files = os.listdir(folder_path)
        
        for file in list_files:
            
            if file.endswith(".csv"):
                
                file_path = os.path.join(folder_path, file)

                print(f"Processing {file}...")

                valid_records = read_csv_file(file_path)
                insert_csv_records(valid_records)
        
        print("CSV data loaded successfully")
    else :
        print("Running analytics...")
        run_analytics()

if __name__ == "__main__":
    main()
