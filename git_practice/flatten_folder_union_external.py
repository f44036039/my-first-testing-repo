import os
from collections import defaultdict

root = 'Trial' # change this
new_directory = 'empireDirectory' # change this
create_diretory_structure_flag = False # Please verify the final_result_list before changing to True

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
#  D1  D2  P    D1   P D1    P  D3   P      # level 2
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
#                                   master_list = [{'G.txt':['ABCD', 'EFGH', ...],          (Every line under jedi/D1/G.txt)
#                                                   'MB.txt':['IJKL','MNOP', ...], ...}, 

#                                                  {'G.txt':['ABCD', 'EFGH', ...],          (Every line under x16/D2/G.txt)
#                                                   'MB.txt':['IJKL','XYNZ', ...], ...}]    (master_list should have 1 to 4 dictionaries, 
#                                                                                            depends on if the D1 is under x20, for example)

# step 3: Merge the dictionaries inside master_list into 1 dictionary using default dictionary, function name: merge_dictionaries
#                                   result_dict = {'G.txt':{'ABCD', 'EFGH', ...},          
#                                                  'MB.txt':{'IJKL','MNOP','XYNZ'...}, ...}

# step 4: Convert this dictioary into a 2d list, function name: create_2d_list
#                                   result_list = [['D1', 'G.txt', 'ABCD', 'EFGH'...],
#                                                  ['D1', 'MB.txt', 'IJKL', 'MNOP','XYNZ'...]...]

# step 5: Append this list to other level 2 directory name list, to create final_result_list, function name: main
#                                    final_result_list = [['D1', 'G.txt', 'ABCD', 'EFGH'...],
#                                                         ['D1', 'MB.txt', 'IJKL', 'MNOP', 'XYNZ'...],
#                                                         ['D2', 'G.txt', 'LEYI', 'WUSK']...]

# step 6: Create file structure based on  final_result_list, function name: create_file_structure

#-------------------------------------------------------------
# function name: get_level_2_set
# read level 2 directories into a set
# output: set_of_level_2 = {'D1', 'D2', ..., 'P'}
#-------------------------------------------------------------
def get_level_2_set(root):

    os.chdir(root)

    level_1_list = []
    for level_1_dir in os.listdir():
        if os.path.isdir(level_1_dir) == True:
            level_1_list.append(level_1_dir)

    # At this part, level_1_list should be ['jedi','x16','x20','x23']

    set_of_level_2 = set()

    for level_1_dir in level_1_list:
        level_2_list = os.listdir(level_1_dir) # for example, everything under jedi, may be ['D1','D2',...]

        for level_2_dir in level_2_list:
            set_of_level_2.add(level_2_dir) # put everything in the list to the set

    return set_of_level_2

#-------------------------------------------------------------------------------------------------------
# function name: create_dict
# create a dictionary containing text file and the content
# output: file_dict = {'G.txt':['ABCD', 'EFGH', ...],      (Every line under jedi / D1 / G.txt)
#                      'MB.txt':['IJKL','MNOP', ...], ...}                      
#-------------------------------------------------------------------------------------------------------

def create_dict(file_list, level_1_dir, folder_name):
    
    file_dict = {}

    for file_name in file_list:
        if os.path.isdir(file_name) == True:
            file_list.remove(file_name)
        
        with open(os.path.join(os.path.join(level_1_dir, folder_name), file_name), 'r') as f: # ex: jedi / D1 / G.txt
            # Create an empty list to store the lines
            lines = []

            # Iterate over the lines of the file
            for line in f:
                # Remove the newline character at the end of the line
                line = line.strip()
                # Append the line to the list
                lines.append(line)

        file_dict[file_name] = lines

    return file_dict

#-------------------------------------------------------------------------------------------------------
# function name: create_list
# create a list of dictionaries
# output: master_list = [{'G.txt':['ABCD', 'EFGH', ...],          (Every line under jedi / D1 / G.txt)
#                        'MB.txt':['IJKL','MNOP', ...], ...}, 

#                       {'G.txt':['ABCD', 'EFGH', ...],          (Every line under x16 / D2 / G.txt)
#                        'MB.txt':['IJKL','XYNZ', ...], ...}]    (master_list should have 1 to 4 dictionaries, 
#                                                                 depends on if the D1 is under x20, for example)
#-------------------------------------------------------------------------------------------------------
def create_list(folder_name):

    level_1_list = []

    for level_1_dir in os.listdir():
        if os.path.isdir(level_1_dir) == True:
            level_1_list.append(level_1_dir)

     # At this part, level_1_list should be ['jedi','x16','x20','x23']

    master_list = []

    for level_1_dir in level_1_list:
        level_2_list = os.listdir(level_1_dir) # for example, everything under jedi, may be ['D10','D11',...]

        if '.DS_Store' in level_2_list:
            level_2_list.remove('.DS_Store') # for Mac

        if folder_name in level_2_list: # for example, D10
            file_list = os.listdir(os.path.join(level_1_dir, folder_name)) # ex: everything under jedi / D10, may be ['G.txt','MB.txt, ...]
            file_dict = create_dict(file_list, level_1_dir, folder_name) # ex: every text data under jedi / D10, {'G.txt':['ABCD', 'EFGH'...],
#                                                                                                                 'MB.txt':['IJKL','MNOP'...], ...}
            master_list.append(file_dict) # append those dictionaries to a list, the list should have 1-4 dictionaries

    return master_list


#-------------------------------------------------------------------------------------------------------
# function name: merge_dictionaries
# Merge the dictionaries inside total_list into 1 dictionary using default dictionary
# output: result_dict = {'G.txt':{'ABCD', 'EFGH', ...},          
#                        'MB.txt':{'IJKL','MNOP','XYNZ'...}, ...}
#-------------------------------------------------------------------------------------------------------

def merge_dictionaries(master_list):

    dd = defaultdict(list)

    for d in (master_list): # master_list has 1-4 dictionaries
        for key, value in d.items():
            dd[key].append(value)

    # dd will be a dictionary with nested lists, ex: {'G.txt':[['ABCD', 'EFGH'...], ['ABCD', 'EFGH'...]],
    #                                                 'MB.txt':[['IJKL', 'MNOP'...], ['IJKL', 'XYNZ'...]] ...}
    # so we want to flatten the nested list and turn it into a set to remove duplicate

    result_dict = {}

    for key, value in dd.items():
        flat_list = [] # flatten the nested list

        for sublist in value:
            for element in sublist:
                flat_list.append(element)

        result_dict[key] = set(flat_list) # turn the flatten list into a set and put into a dictionary

    return result_dict

#-------------------------------------------------------------------------------------------------------
# function name: create_2d_list
# Convert this dictioary into a 2d list
# output: result_list = [['D1', 'G.txt', 'ABCD', 'EFGH'...],
#                        ['D1', 'MB.txt', 'IJKL', 'MNOP','XYNZ'...]...]
#-------------------------------------------------------------------------------------------------------

def create_2d_list(result_dict, dir_name):

    result_list = []

    for key, value in result_dict.items():
        temp_list = [dir_name, key]

        for itr in value:
            temp_list.append(itr)

        result_list.append(temp_list)
    
    return result_list

# ----------------------------------------------------------------------------------------------------------------
# Take the root dir, read everything under the root and create a 2D list containing dir name, file name and conrent
# output:final_result_list = [['D1', 'G.txt', 'ABCD', 'EFGH'...],
#                             ['D1', 'MB.txt', 'IJKL', 'MNOP', 'XYNZ'...],
#                             ['D2', 'G.txt', 'LEYI', 'WUSK']...]
# ---------------------------------------------------------------------------

def main(root):
    set_of_level_2 = get_level_2_set(root) # ex: {'D1', 'D2', ..., 'PLC'}
    set_of_level_2.discard('LastSize.txt')
    final_result_list = []

    for dir_name in set_of_level_2: # ex: 'D1'
        master_list = create_list(dir_name) # ex: [{'G.txt':['ABCD', 'EFGH'...], 'MB.txt':['IJKL','MNOP'...], ...}, 
                                            #      {'G.txt':['ABCD', 'EFGH'...], 'MB.txt':['IJKL','XYNZ'...], ...}]

        result_dict = merge_dictionaries(master_list) # {'G.txt':{'ABCD', 'EFGH', ...}, 'MB.txt':{'IJKL','MNOP','XYNZ'...}, ...}

        result_list = create_2d_list(result_dict, dir_name) # [['D1', 'G.txt', 'ABCD', 'EFGH'...], ['D1', 'MB.txt', 'IJKL', 'MNOP','XYNZ'...]]

        for element in result_list:
            final_result_list.append(element)
                
    return final_result_list


# -----------------------------------------------------------
# function name: create_file_structure
# Create file structure based on final_result_list
#               root
#                |
#         ----------------------
#        |      |       |       |
#       D1     D2      D3       P
#        |      |       |       |
#      G.txt   G.txt  A.txt   G.txt 
# ------------------------------------------------------------


def create_file_structure(result_list, root_dir_name, flag):

    if flag == True:
        os.chdir("..")

        for i in range(len(result_list)): 
            info = result_list[i] # ex: ['D1', 'G.txt', 'ABCD', 'EFGH']
            dir_name = info[0] # ex: 'D1'
            file_name = info[1] # ex: 'G.txt'
            content = info[2:] # ex: ['ABCD', 'EFGH']
            dir_path = os.path.join(root_dir_name, dir_name) # root_dir_name + '/' + dir_name

            if not os.path.exists(dir_path): 
                os.makedirs(dir_path)

            file_path = os.path.join(dir_path, file_name) # root_dir_name + '/' + dir_name + '/' + file_name
            with open(file_path, 'w') as f:
                for line in content:
                    f.write(line)
                    f.write('\n')
    else:
        print('Did not create new file structure')


# --------------------- End of functions

final_result_list = main(root)
print(final_result_list)
create_file_structure(final_result_list, new_directory, create_diretory_structure_flag)
