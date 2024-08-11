from file import File
from folder import Folder

"""
commands : 
cd check
mkdir -> new folder check
mkfile -> new file check
cp -> copy
mv -> cut
rm -> remove check
ls -> print all directories check
filenew -> new text in the file check
fileedit -> edit a line in the file check
cat -> file text check
../ -> goes back check
"""

root_folder = Folder('/')
this_folder = root_folder
folders_list = []
folders_list.append(this_folder)

def find_by_directory(directory : str, this_folder : Folder):
    direction_folders = []
    directory_list = directory.split('/')
    current_folder = this_folder
    current_folder : Folder
    for i in range(len(directory_list)):
        if i == len(directory_list) - 1 :
            if len(directory_list[i].split('.')) == 2:
                file_whole_name = directory_list[i].split('.')
                file = current_folder.search_files_by_name(file_whole_name[0], file_whole_name[1])
                if file == None:
                    print ('no such file or directory')
                    return False , None, None, []
                return True, current_folder, file, direction_folders
            else:
                current_folder = current_folder.search_folders_by_name(directory_list[i])
                if current_folder == None:
                    print('no such file or directory')
                    return False , None , None, []
                direction_folders.append(current_folder)
                return True , current_folder , None, direction_folders

            
        else:
            current_folder = current_folder.search_folders_by_name(directory_list[i])
            if current_folder == None:
                print('no such file or directory')
                return False , None, None, []
            direction_folders.append(current_folder)
def cd(directory, current_folder,folders_list):
    found, new_folder, file, direction_folders= find_by_directory(directory, current_folder)
    if found and file == None:
        for folder in direction_folders:
            folders_list.append(folder)
        return new_folder, folders_list
    return current_folder, folders_list

def back(folders_list):
    if folders_list:
        folders_list.pop()
        current_folder = folders_list[-1]
    return current_folder, folders_list
    


def text_input():
    print("enter your text (0/end/0 = finish)")
    inp = ''
    text = []
    while inp != '0/end/0':
        inp = input('')
        text.append(inp)
    return text

