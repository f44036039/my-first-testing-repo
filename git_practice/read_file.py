import os
import openpyxl

root_dir = 'C:/Users/steven_hsu/Documents/code/test'
os.chdir(root_dir)

level_1_list = []

for level_1_dir in os.listdir():
    if os.path.isdir(level_1_dir) == True:
        level_1_list.append(level_1_dir)

# print(level_1_list)

level_2_list = []
# wb = openpyxl.load_workbook('list.xlsx')


for level_1_dir in level_1_list:
    level_2_dir = os.listdir(os.path.join(root_dir, level_1_dir))
    level_2_list.append(level_2_dir)
    
# print(level_2_list)



result = []

for i in range(len(level_2_list)):
    folder = dict()
    for j in range(len(level_2_list[i])):
        directory = os.path.join(root_dir, level_1_list[i])
        
        folder[level_2_list[i][j]] = os.listdir(os.path.join(directory, os.listdir(directory)[j]))

    result.append(folder)

print(result)
