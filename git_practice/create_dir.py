import os
import pandas as pd

create_folder_structure_flag = False
print("please put the excel file under this directory: ", os.getcwd())
excel_file_name = 'file_structure.xlsx'
data = pd.read_excel(excel_file_name)
print(data)

if create_folder_structure_flag == True:

    for i in range(len(data)):

        info = data.iloc[i,:].dropna()

        dir_name = info[0]

        file_name = info[1]

        content = info[2:]

        root_dir_name = 'empireDirectory_excel'
        dir_path = os.path.join(root_dir_name, dir_name) # root_dir_name + '/' + dir_name

        if not os.path.exists(dir_path): 
            os.makedirs(dir_path)

        file_path = os.path.join(dir_path, file_name)

        with open(file_path, 'w') as f:
            for line in content:
                f.write(line)
                f.write('\n')
else:
    print('Did not create folder structure from excel')
