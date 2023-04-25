import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

puttern = re.compile(r"(8|\+7)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*[-\s]*(\d{2})[-\s]*(\d+)\s*(\(*(доб\.)\s*(\d+)\)*)?")
subst = r"+7(\2)\3-\4-\5 \7\8"

for contact in contacts_list:
    contact[5] = puttern.sub(subst, contact[5])

    valid_name = []
    for i in range(3):
        row = re.findall('\w+', contact[i])
        for j in range(len(row)):
            valid_name.append(row[j])
    for i in range(len(valid_name)):
        contact[i] = valid_name[i]

dupl_dict = {}
dupl_list = []
for contact in enumerate(contacts_list):
    if contact[1][0] in dupl_dict:
        i = dupl_dict[contact[1][0]]
        if contact[1][1] == contacts_list[i][1]:
            dupl_list.append(contact[0])
        else: dupl_dict[contact[1][0]] = contact[0]
    else: dupl_dict[contact[1][0]] = contact[0]

for i in dupl_list:
    j = dupl_dict[contacts_list[i][0]]
    for k in range(3, 7):
        if contacts_list[j][k] == '':
            contacts_list[j][k] = contacts_list[i][k]

n = 0
for i in dupl_list:
    del contacts_list[i - n]
    n += 1

pprint(contacts_list)
with open("phonebook_new.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
  datawriter.writerows(contacts_list)