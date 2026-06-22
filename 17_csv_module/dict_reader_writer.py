import csv

with open("random_names.csv", "r") as csv_file:
    # Dict reader by default assumes 1st row is header. They will be key names by default.
    # In case csv file does not have headers, specify fieldnames arg. Same as in write dict example below
    reader = csv.DictReader(csv_file)
    for line in reader:
        print(line)


with open("random_names.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    with open("new_names_2.csv", "w") as w_file:
        fieldnames = ["firstname", "lastname"]
        writer = csv.DictWriter(w_file, delimiter="-", fieldnames=fieldnames)
        # Must be explicitly written as reader will not have the headers. Because each row is not a dict 
        writer.writeheader()
        for line in reader:
            del line["email"]
            writer.writerow(line)
