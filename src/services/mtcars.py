import os
import csv

MTCARS_file = "./services/mtcars.csv"

MTCARS = []

if os.path.exists(MTCARS_file):
    with open(MTCARS_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            MTCARS.append(row)

else: 
    print("MTCARS file not found")