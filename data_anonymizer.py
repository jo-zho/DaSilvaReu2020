""" description: for every file in a directory, 
    renames the file to its hash value and writes 
    to a file the association between each key and 
    hash value. zips renamed files
"""
import os  # for renaming
import shutil  # for archiving

# TODO: implement collision checking and workound in case of collision

# get file path from user
file_path = input("What is the file path of the directory you want to anonymize? ")

# create text file with association b/w keys and hashed values
f = open(f'{file_path}/keys.txt', "w")

# renames each file in directory to its hash value
print("Hashing files...")
for file in os.listdir(file_path):
    # name of file excluding email suffix
    username = file.split('@')[0]
    if file == "keys.txt":  # skips file holding keys
        continue
    # write to file association between username and hash(filename)
    f.write(f'{username}, {hash(username)} \n')  # formatted for CSV
    # renaming file to its hash
    os.rename(f'{file_path}/{file}', f'{file_path}/{hash(username)}@tamu.edu')

f.close()

# zips files in "anonymous_data.zip" to directory above directory being archived
print("Creating zip...")
dir_above = os.path.dirname(file_path)
print(dir_above)
shutil.make_archive(f'{dir_above}/anonymous_data', "zip", file_path)

