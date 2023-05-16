import os
import openpyxl

os.chdir('Trial')
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

jedi_dict = {}
jedi_set = set()

for file_name in jedi_list:
        
    with open(os.path.join(os.path.join(level_1_list[0],folder_name),file_name), 'r') as f:
        # Create an empty list to store the lines
        lines = []

        # Iterate over the lines of the file
        for line in f:
            # Remove the newline character at the end of the line
            line = line.strip()

            # Append the line to the list
            lines.append(line)
    jedi_dict[file_name] = lines

print(jedi_dict)
# print(len(jedi_dict))
# print(len(jedi_dict['SB.txt']))

x16_dict = {}
x16_set = set()

for file_name in x16_list:
        
    with open(os.path.join(os.path.join(level_1_list[1],folder_name),file_name), 'r') as f:
        # Create an empty list to store the lines
        lines = []

        # Iterate over the lines of the file
        for line in f:
            # Remove the newline character at the end of the line
            line = line.strip()

            # Append the line to the list
            lines.append(line)
    x16_dict[file_name] = lines

print(x16_dict)
# print(len(x16_dict))
# print(len(x16_dict['SB.txt']))

print(jedi_list)
print(x16_list)

common = set(jedi_list).union(set(x16_list))
print(common)

wb = openpyxl.Workbook()
ws = wb.active

for element in common:
    if element in jedi_dict and element in x16_dict:
        result = set(jedi_dict[element]).union(set(x16_dict[element]))
    else:
        if element in jedi_dict:
            result = set(jedi_dict[element])
        if element in x16_dict:
            result = set(x16_dict[element])

    list1 = list(result)
    ws.append(list1)
wb.save('try.xlsx')

