from file import File
from folder import Folder

"""
commands : 
cd 
mkdir -> new folder
mkfile -> new file
cp -> copy
mv -> cut
rm -> remove
ls -> print all directories
filenew -> new text in the file
fileedit -> edit a line in the file 
cat -> file text
../ -> goes back
"""

root_folder = Folder('/')
this_folder = root_folder

def find_by_directory(directory : str, this_folder : Folder):
    if directory[0] != '/' and this_folder.get_name() == '/':
        print('no such file of directory')
        return False, None, None
    if this_folder.get_name() == '/':
        directory_list = directory.split('/')
        del directory_list[0]
    current_folder = this_folder
    current_folder : Folder
    for i in range(len(directory_list)):
        if i == len(directory_list) - 1 :
            if len(directory_list[i].split('.')) == 2:
                file_whole_name = directory_list[i].split('.')
                file = current_folder.search_files_by_name(file_whole_name[0], file_whole_name[1])
                if file == None:
                    print ('no such file or directory')
                    return False , None, None
                return True, current_folder, file
            else:
                current_folder = current_folder.search_folders_by_name(directory_list[i])
                if current_folder == None:
                    print('no such file or directory')
                    return False , None , None
                return True , current_folder , None

            
        else:
            current_folder = current_folder.search_folders_by_name(directory_list[i])
            if current_folder == None:
                print('no such file or directory')
                return False , None

def text_input():
    print("enter your text (0/end/0 = finish)")
    inp = ''
    text = []
    while inp != '0/end/0':
        inp = input('')
        text.append(inp)
    return text

