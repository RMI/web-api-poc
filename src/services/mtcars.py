import csv

# define mtcars filepath 
MTCARS_file = "./data/mtcars.csv"

#open mtcars file and read into dictionary
def csv_to_dict(MTCARS_file):
    mtcars = {}
    with open(MTCARS_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Assuming the first column is a unique key
            key = row[csv_reader.fieldnames[0]].replace(" ", "")
            mtcars[key] = row
    return mtcars

# call csv to dict function
MTCARS = csv_to_dict(MTCARS_file)