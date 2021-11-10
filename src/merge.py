import os
import pandas as pd

# input
input_dir = 'eoac'
exclude_dirs = ['provincia_fail', 'output']
output_dir = 'eoac/output'

# loop over all directories in input_dir
input_dir_path, output_dir_path = '../' + input_dir, '../' + output_dir
for files_dir in list(filter(lambda val: not val.startswith('.') and val not in exclude_dirs, os.listdir(input_dir_path))):
    files_dir_path = input_dir_path + '/' + files_dir
    output_xls_file_path = output_dir_path + f'/{input_dir}_{files_dir}_all.xls'

    xls_files = []

    # exclude hidden files (e.g. '.DS_Store')
    for file_path in list(filter(lambda val: not val.startswith('.'), os.listdir(files_dir_path))):
        try:
            xls_file = pd.read_excel(files_dir_path + '/' + file_path)
        except:
            print('ERROR at file:' + files_dir_path + '/' + file_path + '\n\n')
        xls_files.append(xls_file)

    df = pd.concat(xls_files, ignore_index=True)
    df.to_excel(output_xls_file_path)
