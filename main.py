from file import File
from folder import Folder

root_folder = Folder('/')
this_folder = root_folder

def find_by_directory(directory : str, this_folder : Folder):
    if directory[0] != '/' and this_folder.get_name() == '/':
        print('no such file of directory')
        return 
    if this_folder.get_name() == '/':
        directory_list = directory.split('/')
        del directory_list[0]

