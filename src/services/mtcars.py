import csv
from importlib import resources


def csv_to_dict(csv_path):
    mtcars = {}
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Assuming the first column is a unique key
            key = row[csv_reader.fieldnames[0]].replace(" ", "")
            mtcars[key] = row
    return mtcars


with resources.path('data', 'mtcars.csv') as mtcars_path:
    MTCARS = csv_to_dict(mtcars_path)
