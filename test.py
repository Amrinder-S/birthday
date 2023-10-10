import csv
import json
from datetime import datetime
import os
os.system("del data.json")
os.system("git add *")
os.system("git commit -m 'delete-old-birthday'")
# Function to load existing JSON data from the file
def load_json_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

# Function to add a new entry to the JSON data
def add_entry(data, name, crn, gender):
    new_entry = {
        "name": name,
        "CRN": crn,
        "gender": gender
    }
    data.append(new_entry)

# Function to save JSON data to the file
def save_json_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to check if today is the birthday
def is_birthday(birthdate):
    today = datetime.now().date()
    formatted_date = today.strftime("%d-%m")
    #print(f"today: {formatted_date} | date: {birthdate[:-5]}")
    return formatted_date == birthdate[:-5]


def main():
    filename = "data.json"
    data = load_json_data(filename)

    # Clear existing data in data.json
    data = []

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name = row["name"]
            crn = row["crn"]
            gender = row["gender"]
            birthdate = row["birthdate"]

            if is_birthday(birthdate):
                add_entry(data, name, crn, gender)

    save_json_data(filename, data)
    os.system("git add *")
    os.system("git commit -m 'birthday-update'")
if __name__ == "__main__":
    main()
