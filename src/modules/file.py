import os

CURR_DIR = os.getcwd()
STORAGE_PATH = f"{CURR_DIR}\\storage\\"

if(not os.path.exists(STORAGE_PATH)):
    os.makedirs(STORAGE_PATH)

def get_file(fname: str):
    return f"{STORAGE_PATH}{fname}"

def remove_file(fname: str):
    os.rmdir(f"{STORAGE_PATH}{fname}")

def create_storage(sname: str):
    new_storage = f"{STORAGE_PATH}{sname}\\"
    print(new_storage)
    if(not os.path.exists(new_storage)):
        os.makedirs(new_storage) 
    return new_storage

