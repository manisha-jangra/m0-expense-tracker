import csv
from validate import Record


def read_csv_file(file_path):

    # create empty list
    valid_records = []
    # open file
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        # loop through each line
        for row in reader:
            try:
                record = Record(**row)
                valid_records.append(record)
                
            except Exception as e:
                print("Invalid data:", row)

    return valid_records