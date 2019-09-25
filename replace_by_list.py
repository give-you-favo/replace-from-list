import glob
import csv
import os

def read_csv_list(csv_path):
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        csv_list = [r for r in reader]
    return csv_list

def get_file_list(path_name):
    return glob.glob(path_name)

def replace_and_write(file, file_to_write, replace_list):
    with open(file, mode="r", encoding="utf-8") as f:
        data = f.read()
    with open(file_to_write, mode="w", encoding="utf-8") as f:
        for replace_pair in replace_list:
            data = data.replace(replace_pair[0], replace_pair[1])
        f.write(data)

def replace_by_list(target_path_name, dist_folder, csv_path):
    file_list = get_file_list(target_path_name)
    replace_list = read_csv_list(csv_path)
    if not os.path.exists(dist_folder):
        os.mkdir(dist_folder)
    for file in file_list:
        filename = os.path.basename(file)
        replace_and_write(file, dist_folder + filename, replace_list)

CSV_PATH = r"list.csv"
TARGET_FOLDER_PATH = r"target/"
DIST_FOLDER_PATH = r"dist/"
replace_by_list(TARGET_FOLDER_PATH + "*.txt", DIST_FOLDER_PATH, CSV_PATH)

