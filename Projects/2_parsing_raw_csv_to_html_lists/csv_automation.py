import csv

html_lists = []

def parsing_like_a_txt_file():
    with open("raw_patreon_contributors.csv", "r") as csv_file:
        next(csv_file)
        next(csv_file)
        next(csv_file)
        next(csv_file)
        for line in csv_file:
            if "No reward" in line:
                break
            data = line.split(",")
            firstname = data[0]
            lastname = data[1]
            html_list = f"<li>{firstname} {lastname}</li>"
            html_lists.append(html_list)

def using_csv_reader():
    with open("raw_patreon_contributors.csv", "r") as csv_file:
        csv_data = csv.reader(csv_file)
        next(csv_data)
        next(csv_data)
        next(csv_data)
        next(csv_data)
        for data in csv_data:
            firstname = data[0]
            if firstname == "No Reward":
                break
            lastname = data[1]
            html_list = f"<li>{firstname} {lastname}</li>"
            html_lists.append(html_list)

def using_csv_dict_reader():
    with open("raw_patreon_contributors.csv", "r") as csv_file:
        csv_data = csv.DictReader(csv_file)
        for data in csv_data:
            firstname = data["FirstName"]
            if "1 + Reward" in firstname:
                continue
            if "Reward" in data["FirstName"]:
                break
            lastname = data["LastName"]
            html_list = f"<li>{firstname} {lastname}</li>"
            html_lists.append(html_list)

if __name__ == "__main__":
    using_csv_dict_reader()

    html_string = f"<h1>There are total {len(html_lists)} public contributors</h1>\n\n\n"

    html_string += "<ul>\n"

    for li in html_lists:
        html_string += f"\t{li}\n"

    html_string += "<ul>"

    with open("contributors.html", "w") as cf:
        cf.write(html_string)