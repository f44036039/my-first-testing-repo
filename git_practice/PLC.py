import os
from collections import defaultdict
import openpyxl

# os.chdir('/Users/xuhaoxiang/Documents/test_2') # for mac
os.chdir('Trial') # for ASUS
# print(os.getcwd())
# print(os.listdir())

root = 'Trial'
level_1_list = os.listdir()
# print(level_1_list)
folder_name = 'PLC'
jedi_list = os.listdir(os.path.join(level_1_list[0],folder_name))
x16_list = os.listdir(os.path.join(level_1_list[1],folder_name))
x20_list = os.listdir(os.path.join(level_1_list[2],folder_name))
x23_list = os.listdir(os.path.join(level_1_list[3],folder_name))

'''print(jedi_list)
print(x16_list)
print(x20_list)
print(x23_list)'''

def create_dict(name_list,i):
    
    name_dict = {}
    name_set = set()
    # print(name_list)

    for file_name in name_list:
        
        with open(os.path.join(os.path.join(level_1_list[i],folder_name),file_name), 'r') as f:
            # Create an empty list to store the lines
            lines = []

            # Iterate over the lines of the file
            for line in f:
                # Remove the newline character at the end of the line
                line = line.strip()

                # Append the line to the list
                lines.append(line)
        name_dict[file_name] = lines

    return name_dict


jedi_dict = create_dict(jedi_list, 0)
x16_dict = create_dict(x16_list, 1)
x20_dict = create_dict(x20_list, 2)
x23_dict = create_dict(x23_list, 3)

'''print(jedi_dict)
print(x16_dict)
print(x20_dict)
print(x23_dict)'''

dd = defaultdict(list)

for d in (jedi_dict, x16_dict, x20_dict, x23_dict):
    for key, value in d.items():
        dd[key].append(value)

# print(dd)

result = {}

for key, value in dd.items():
    flat_list = []
    for sublist in value:
        for element in sublist:
            flat_list.append(element)
    result[key] = set(flat_list)

print(result)

wb = openpyxl.Workbook()
ws = wb.active

for key, value in result.items():
    list1 = [folder_name ,key]
    for itr in value:
        list1.append(itr)
    ws.append(list1)

wb.save('try.xlsx')
