import sys
from db import insert_csv_records
from csv_reader import read_csv_file
from analytics import run_analytics

def main():
    # check if argument is passed
    if len(sys.argv) > 1 and sys.argv[1] == "ingest":
        
        print("Running CSV ingestion...")
        file_path = "data/expense_1.csv"
        # gives valid records
        valid_records = read_csv_file(file_path)
        # this inserted the valid record in postgres
        insert_csv_records(valid_records)
        
        print("CSV data loaded successfully")
    else :
        print("Running analytics...")
        run_analytics()

if __name__ == "__main__":
    main()
