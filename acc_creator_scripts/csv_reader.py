import csv
import random
from faker import Faker
from datetime import datetime

faker = Faker()
rows = []
with open("user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        print(row[1])
        birthDate = datetime.fromisoformat(row[2])
        day = str(f"{birthDate.day:02}")
        month = str(f"{birthDate.month:02}")

        row[3] = row[1].lower().replace(" ", "") +\
                 day + \
                 month + str(birthDate.year) + '@gmail.com'
        if row[1] == '':
            name = faker.name_female() \
                .replace("Ms. ", "") \
                .replace("Mrs. ", "") \
                .replace("Dr. ", "") \
                .replace("MD. ", "") \
                .replace("DVM ", "") \
                .replace("DDS ", "")
            row[1] = name
            yearOfBirth = str(random.randint(1980, 2002))
            row[2] = yearOfBirth + '-' + faker.date_of_birth().strftime("%m-%d")
            row[3] = name.lower().replace(" ", "") + yearOfBirth + '@gmail.com'

        rows.append(row)

filename = 'user_db_updated.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header) + ',')
    file.write('\n')
    for row in rows:
        print(row)
        for x in row:
            file.write(x + ',')
        file.write('\n')

print('=============================================')

with open("user_db_updated.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        rows.append(row)
        print(row)
