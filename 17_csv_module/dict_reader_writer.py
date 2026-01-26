import csv

with open("random_names.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        print(line)


with open("random_names.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    with open("new_names_2.csv", "w") as w_file:
        fieldnames = ["firstname", "lastname"]
        writer = csv.DictWriter(w_file, delimiter="-", fieldnames=fieldnames)
        writer.writeheader()
        for line in reader:
            del line["email"]
            writer.writerow(line)
