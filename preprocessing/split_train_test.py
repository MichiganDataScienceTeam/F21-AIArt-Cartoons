import os
import random
import shutil

source = 'folder_path_1' # need to change
dest = 'dest_folder_path' # need to change
files = os.listdir(source)
num_of_files = len(files) // 2.5 

for file_name in random.sample(files, num_of_files):
    shutil.move(os.path.join(source, file_name), dest)
