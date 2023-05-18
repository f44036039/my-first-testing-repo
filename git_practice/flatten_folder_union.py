import os
import openpyxl
from collections import defaultdict

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

    # print(level_1_list)
    total_list = []
    set_of_level_2 = set()

    for i in range(len(level_1_list)):
        level_2_list = os.listdir(level_1_list[i])

        if '.DS_Store' in level_2_list:
            level_2_list.remove('.DS_Store') # for Mac

        for itr in level_2_list:
            set_of_level_2.add(itr)

        if folder_name in level_2_list:
            file_list = os.listdir(os.path.join(level_1_list[i],folder_name))
            file_dict = create_dict(file_list, i, level_1_list, folder_name)
            total_list.append(file_dict)

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


def create_2d_list(result,dir_name):

    result_list = []

    for key, value in result.items():
        list1 = [dir_name ,key]
        for itr in value:
            list1.append(itr)
        result_list.append(list1)

    '''wb = openpyxl.load_workbook('/Users/xuhaoxiang/code/empire.xlsx')
    ws = wb.active
    print(result)
    
        # print(list1)

    os.chdir('/Users/xuhaoxiang/code')
    wb.save('empire.xlsx')'''
    
    return result_list


def main(root):
    set_of_level_2 = get_level_2_set(root)
    print(set_of_level_2)

    for dir_name in set_of_level_2:

        total_list = create_list(dir_name)
        # print(total_list)
        result = create_default_dict(total_list)
        result_list = create_2d_list(result,dir_name)
        
        return result_list

def create_file_structure(result_list, root_dir_name):

    for i in range(len(result_list)):

        info = result_list[i]

        dir_name = info[0]

        file_name = info[1]

        content = info[2:]

        if not os.path.exists(root_dir_name + '/' + dir_name):
            os.makedirs(root_dir_name + '/' + dir_name)

        with open(root_dir_name + '/' + dir_name + '/' + file_name, 'w') as f:
            for line in content:
                f.write(line)
                f.write('\n')

# root = 'Trial' # for ASUS
root = '/Users/xuhaoxiang/Documents/test_2' # for Mac
result_list = main(root)
create_file_structure(result_list, 'empireDirectory')