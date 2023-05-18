import os
import pandas as pd

data = pd.read_excel('empire.xlsx')
print(data)

for i in range(len(data)):

    info = data.iloc[i,:].dropna()

    dir_name = info[0]

    file_name = info[1]

    content = info[2:]

    root_dir_name = 'empireDirectory'
    if not os.path.exists(root_dir_name + '/' + dir_name):
        os.makedirs(root_dir_name + '/' + dir_name)

    with open(root_dir_name + '/' + dir_name + '/' + file_name, 'w') as f:
        for line in content:
            f.write(line)
            f.write('\n')
