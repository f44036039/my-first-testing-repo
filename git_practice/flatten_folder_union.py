import os
import openpyxl
from collections import defaultdict


def create_dict(level_3_list,i, level_1_list, folder_name):
    
    level_3_dict = {}

    for file_name in level_3_list:
        
        with open(os.path.join(os.path.join(level_1_list[i],folder_name),file_name), 'r') as f:
            # Create an empty list to store the lines
            lines = []

            # Iterate over the lines of the file
            for line in f:
                # Remove the newline character at the end of the line
                line = line.strip()

                # Append the line to the list
                lines.append(line)
        level_3_dict[file_name] = lines

    return level_3_dict

def create_list(folder_name):

    level_1_list = []
    for level_1_dir in os.listdir():
        if os.path.isdir(level_1_dir) == True:
            level_1_list.append(level_1_dir)


    total_list = []
    set_of_level_2 = set()

    for i in range(len(level_1_list)):
        level_2_list = os.listdir(level_1_list[i])
        for itr in level_2_list:
            set_of_level_2.add(itr)

        if folder_name in level_2_list:
            jedi_list = os.listdir(os.path.join(level_1_list[i],folder_name))
            jedi_dict = create_dict(jedi_list, i, level_1_list, folder_name)
            total_list.append(jedi_dict)


    return total_list



def create_default_dict(total_list):
    dd = defaultdict(list)
    for d in (total_list):
        for key, value in d.items():
            dd[key].append(value)

    result = {}

    for key, value in dd.items():
        flat_list = []
        for sublist in value:
            for element in sublist:
                flat_list.append(element)
        result[key] = set(flat_list)

    return result


def create_excel(result,dir_name):
    wb = openpyxl.load_workbook('C:/Users/steven_hsu/Documents/code/empire.xlsx')
    ws = wb.active

    for key, value in result.items():
        list1 = [dir_name ,key]
        for itr in value:
            list1.append(itr)
        ws.append(list1)

    os.chdir('C:/Users/steven_hsu/Documents/code')
    wb.save('empire.xlsx')

def get_level_2_set(root):

    os.chdir(root)

    level_1_list = []
    for level_1_dir in os.listdir():
        if os.path.isdir(level_1_dir) == True:
            level_1_list.append(level_1_dir)

    set_of_level_2 = set()

    for i in range(len(level_1_list)):
        level_2_list = os.listdir(level_1_list[i])
        for itr in level_2_list:
            set_of_level_2.add(itr)

    return set_of_level_2

def main(root):
    set_of_level_2 = get_level_2_set(root)

    for dir_name in set_of_level_2:

        total_list = create_list(dir_name)
        result = create_default_dict(total_list)
        create_excel(result,dir_name)

root = 'Trial'
main(root)

