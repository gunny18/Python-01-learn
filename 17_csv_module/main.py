import csv

with open("random_names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)

print("===========================================================")

with open("random_names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)

print("===========================================================")
with open("random_names.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    with open("new_names.csv", "w") as w_file:
        writer = csv.writer(w_file, delimiter=".")

        for line in reader:
            writer.writerow(line)

print("===========================================================")
with open("new_names.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=".")
    for line in reader:
        print(line)
