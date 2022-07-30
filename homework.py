import re
import csv

# clear phonebook.csv from old data
with open('phonebook.csv', 'w'):
    pass

# read phone book phonebook_raw.csv to contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# convert contacts list to string
id = 0
contacts_list_string = []
for i in contacts_list:
    if id == 0:
        contact = str(f'id,')
    else:
        contact = str(f'{id},')
    id += 1
    for j in i:
        contact += j + ','
    contact = contact[:-1]
    contacts_list_string.append(contact)

# create dict keys
for i in contacts_list_string:
    key_list_for_dict = i.split(',')
    break

# text generator to hregex101.com
# for i in contacts_list_string:
    # print(i)

# raw contacts list generator
first_string = 0
contacts_list_string_2 = []
for i in contacts_list_string:
    if first_string == 0:
        first_string += 1
        continue
    else:
        pattern = re.compile(r'^(\d),(\w+)?( |,)(\w+)?( |,)(\w+)?(,{1,3})(\w+)?,(.*),((\+7|8)( )?(\()?(\d\d\d)(\))?( '
                             r'|-)?(\d\d\d)( |-)?(\d\d)( |-)?(\d\d)( )?(\()?(доб\.)?( )?(\d+)?(\))?)?,(.*)?')
        result_2 = pattern.sub("\\1,\\2,\\4,\\6,\\8,\\9,+7(\\14)\\17-\\19-\\21 \\24\\26,\\28", i)
        contacts_list_string_2.append(result_2)

# create data in dict format
almost_clear_contacts_list = []
for i in contacts_list_string_2:
    a = i.split(',')
    dict_from_list = dict(zip(key_list_for_dict, a))
    almost_clear_contacts_list.append(dict_from_list)

# create almost clear contacts list (have duplicate)
temp_name_list = []
for i in range(len(almost_clear_contacts_list)):
    if almost_clear_contacts_list[i]['lastname'] not in temp_name_list:
        temp_name_list.append(almost_clear_contacts_list[i]['lastname'])
        continue
    else:
        for j in almost_clear_contacts_list:
            if j['lastname'] == almost_clear_contacts_list[i]['lastname']:
                for k in key_list_for_dict:
                    if j[k] == '' or j[k] == '+7()-- ':
                        j[k] = almost_clear_contacts_list[i][k]
                        pass
            else:
                continue

clear_contacts_list = []
temp_name_list = []
for i in range(len(almost_clear_contacts_list)):
    # print(i)
    if almost_clear_contacts_list[i]['lastname'] not in temp_name_list:
        temp_name_list.append(almost_clear_contacts_list[i]['lastname'])
        clear_contacts_list.append(almost_clear_contacts_list[i])
        continue
    else:
        continue

# create phonebook.csv with clear data
with open("phonebook.csv", "a") as f:
    datawriter = csv.DictWriter(f, fieldnames=key_list_for_dict)
    datawriter.writeheader()
    datawriter.writerows(clear_contacts_list)
