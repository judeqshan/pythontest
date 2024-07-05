import csv

# Open the CSV file and read its contents
with open('input_data.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)