import os
from collections import defaultdict

root = 'Trial' # change this
new_directory = 'empireDirectory' # change this
create_diretory_structure_flag = True # Please verify the final_result_list before changing to True

# ------------------------------------------------------------------------------------------
# Problem Statement:
# Before:
#               root
#                |
#          ----------------------
#         |      |       |       |
#       jedi    x16     x20     x23         # level 1
#         |      |       |       |
#   --------    -----   -----   -----
#   |   |  |    |    |  |    |  |    |
#  D1  D2  P    D1   P D1    P  D3   P    # level 2
#   |   |  |    |    |  |    |  |    |
#  G.txt   G.txt  G.txt   G.txt A.txt       # level 3 (or file)

# Combine everything under G.txt level, then create file structure as
# After :
#               root
#                |
#         ----------------------
#        |      |       |       |
#       D1     D2      D3       P
#        |      |       |       |
#      G.txt   G.txt  A.txt   G.txt 

# The content under D1 / G.txt should not be mixed with D2 / G.txt or P / G.txt
#------------------------------------------------------------------------------------------------

# Sol step:
# step 1, read level 2 directories into a set, set_of_level_2 = {'D1', 'D2', ..., 'P'},   function name: get_level_2_set

# step 2: for every element inside this set, for example, 'D1', create a list of dictionaries,functiona name: create_list, create_dict
#                                   total_list = [{'G.txt':['ODXP', 'ODYP', ...],          (Every line under jedi/D1/G.txt)
#                                                  'MB.txt':['HDXP','HDDP', ...], ...}, 

#                                                 {'G.txt':['ODXP', 'ODYP', ...],          (Every line under x16/D2/G.txt)
#                                                  'MB.txt':['HDXP','HDDP', ...], ...}]    (total_list should have 1 to 4 dictionaries, 
#                                                                                           depends on if the D1 is under x20, for example)

# step 3: Merge the dictionaries inside total_list into 1 dictionary using default dictionary, function name: create_default_dict
#                                   result = {'G.txt':{'ODXP', 'ODYP', ...},          
#                                             'MB.txt':{'HDXP','HDDP', ...}, ...}

# step 4: Convert this dictioary into a 2d list, function name: create_2d_list
#                                   result_list = [['D1', 'G.txt', 'ODXP', 'ODYP'...],
#                                                  ['D1', 'MB.txt', 'HDXP', 'HDDP'...]...]

# step 5: Append this list to other level 2 directory name list, to create final_result_list, function name: main
#                                    final_result_list = [['D1', 'G.txt', 'ODXP', 'ODYP'...],
#                                                         ['D1', 'MB.txt', 'HDXP', 'HDDP'...],
#                                                         ['D2',  'G.txt', 'ABCD', 'HGDJ']...]

# step 6: Create file structure based on  final_result_list, function name: create_file_structure

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
        if os.path.isdir(file_name) == True:
            # print('found file')
            level_3_list.remove(file_name)
        
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

    for i in range(len(level_1_list)):
        level_2_list = os.listdir(level_1_list[i])

        if '.DS_Store' in level_2_list:
            level_2_list.remove('.DS_Store') # for Mac

        if 'LastSize.txt' in level_2_list:
                level_2_list.remove('LastSize.txt')

        if folder_name in level_2_list:
            file_list = os.listdir(os.path.join(level_1_list[i],folder_name))
            if 'LastSize.txt' in file_list:
                file_list.remove('LastSize.txt')
            level_3_dict = create_dict(file_list, i, level_1_list, folder_name)
            total_list.append(level_3_dict)

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
    
    return result_list


def main(root):
    set_of_level_2 = get_level_2_set(root)
    set_of_level_2.discard('LastSize.txt')

    final_result_list = []

    for dir_name in set_of_level_2:

        total_list = create_list(dir_name)
        print(total_list)
        result = create_default_dict(total_list)
        master_list = create_2d_list(result,dir_name)
        for element in master_list:
            final_result_list.append(element)
                
    return final_result_list


def create_file_structure(result_list, root_dir_name, flag):

    if flag == True:
        os.chdir("..")
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

final_result_list = main(root)
print(final_result_list)
create_file_structure(final_result_list,new_directory, create_diretory_structure_flag)