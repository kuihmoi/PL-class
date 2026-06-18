import csv  # importing data
from typing import List, Dict 

#defines two python function to process csv files using typing modules

#this function is to read csv file and return its content as a list of dictionaries
def load_csv_file(file_path: str) -> List[Dict]: #list[dict] from typing modules
    data = []  #data has nothing at the beginning
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)  #add all rows from the data.csv
    return data

#extract one column from csv file
def extract_column(data: List[Dict], column_name: str) -> List[float]: #list containing floating point numbers
    return [float(item[column_name]) for item in data]