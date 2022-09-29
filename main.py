import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contact_list = list(rows)

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substitution = r'+7(\2)-\3-\4-\5 \6\7'
step_list = list()
correct_list = list()

for item in contact_list:
    fio = ' '.join(item[:3]).split(' ')
    lastname = fio[0]
    firstname = fio[1]
    surname = fio[2]
    organization = item[3]
    position = item[4]
    phone = re.sub(pattern, substitution, item[5])
    email = item[6]
    step_list.append([lastname, firstname, surname, organization, position, phone, email])

for item in step_list:
    for step in step_list:
        if item[0] == step[0] and item[1] == step[1]:
            if item[2] == '':
                item[2] = step[2]
            if item[3] == '':
                item[3] = step[3]
            if item[4] == '':
                item[4] = step[4]
            if item[5] == '':
                item[5] = step[5]
            if item[6] == '':
                item[6] = step[6]
    if item not in correct_list:
        correct_list.append(item)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(correct_list)
