from file import File
from folder import Folder

"""
commands : 
cd check
mkdir -> new folder check
mkfile -> new file check
cp -> copy
mv -> cut
rm -> rmv check
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

def find_by_directory(directory : str, this_folder : Folder, root_folder : Folder):
    direction_folders = []
    if directory[0] == '/':
        del directory[0]
        current_folder = root_folder
    else:
        current_folder = this_folder
    directory_list = directory.split('/')
    current_folder : Folder
    for i in range(len(directory_list)):
        if i == len(directory_list) - 1 :
            if len(directory_list[i].split('.')) == 2:
                file_whole_name = directory_list[i].split('.')
                file = current_folder.search_files_by_name(file_whole_name[0], file_whole_name[1])
                if file == None:
                    print ('no such file or directory')
                    return False , current_folder, None, direction_folders
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
def cd(directory, current_folder,folders_list, root_folder):
    if directory[0] != '/':
        flag = 0
    else:
        flag = 1
    found, new_folder, file, direction_folders= find_by_directory(directory, current_folder, root_folder)
    if found and file == None and flag == 0:
        for folder in direction_folders:
            folders_list.append(folder)
        return new_folder, folders_list
    elif found and file == None and flag == 1 :
        folders_list = direction_folders

    return current_folder, folders_list

def back(folders_list):
    if folders_list:
        folders_list.pop()
        current_folder = folders_list[-1]
    return current_folder, folders_list



def move_file_to_file(source_path: str, destination_path: str, this_folder : Folder, root_folder):
    found_source, source_folder, source_file, _ = find_by_directory(source_path,  this_folder, root_folder )
    found_destination, destination_folder, destination_file, _ = find_by_directory(destination_path,  this_folder, root_folder )
    if not found_source or source_file == None :
        print("Source file not found")
        return False
    elif destination_folder == None:
        print("Destination folder not found")
        return False
    else:
        file_text = source_file.get_text()
        if destination_file != None:
            first_text = destination_file.get_text()
            file_text = first_text + file_text
            destination_file.new_text(file_text)
        else:
            new_file_whole_name = destination_path.split('/')[-1]
            new_file_name = new_file_whole_name.split('.')[0]
            new_file_format = new_file_whole_name.split('.')[1]
            destination_folder.add_file(new_file_name, new_file_format)
            new_file = destination_folder.search_files_by_name(new_file_name, new_file_format)
            new_file.new_text(file_text)


        source_folder.rmv(source_path.split('/')[-1])
        return True

def copy_file_to_file(source_path: str, destination_path: str, this_folder : Folder, root_folder):
    found_source, source_folder, source_file, _ = find_by_directory(source_path,  this_folder, root_folder )
    found_destination, destination_folder, destination_file, _ = find_by_directory(destination_path,  this_folder, root_folder )
    if not found_source or source_file == None :
        print("Source file not found")
        return False
    elif destination_folder == None:
        print("Destination folder not found")
        return False
    else:
        file_text = source_file.get_text()
        if destination_file != None:
            first_text = destination_file.get_text()
            file_text = first_text + file_text
            destination_file.new_text(file_text)
        else:
            new_file_whole_name = destination_path.split('/')[-1]
            new_file_name = new_file_whole_name.split('.')[0]
            new_file_format = new_file_whole_name.split('.')[1]
            destination_folder.add_file(new_file_name, new_file_format)
            new_file = destination_folder.search_files_by_name(new_file_name, new_file_format)
            new_file.new_text(file_text)

        return True

def text_input():
    print("enter your text (0/end/0 = finish)")
    inp = ''
    text = []
    while inp != '0/end/0':
        inp = input('')
        text.append(inp)
    return text

def copy_folder_to_folder(source_path: str , destination_path: str , this_folder : Folder, root_folder) :
    found_source , source_folder , _, _ = find_by_directory(source_path , this_folder, root_folder)
    found_destination , destination_folder, _, _ = find_by_directory(destination_path , this_folder, root_folder)
    if not found_source or source_folder == None :
        print("source folder was not found")
        return False
    elif destination_folder == None or not found_destination :
        print("destination folder was not found")
        return False
    else:
        source_folder.folder_adder(destination_folder)

def move_folder_to_folder(source_path: str , destination_path: str , this_folder : Folder, root_folder) :
    found_source , source_folder , _, source_folders = find_by_directory(source_path , this_folder, root_folder)
    found_destination , destination_folder, _, _ = find_by_directory(destination_path , this_folder, root_folder)
    if not found_source or source_folder == None :
        print("source folder was not found")
        return False
    elif destination_folder == None or not found_destination :
        print("destination folder was not found")
        return False
    else:
        destination_folder.folder_adder(source_folder)
        source_folders[-2].rmv(source_folders[-1].get_name())

def cat(file_path, this_folder, root_folder):
    found_file, _ , current_file, _ = find_by_directory(file_path,  this_folder, root_folder )
    if found_file and current_file != None:
        current_file : File
        text_list = current_file.get_text()
        for text in text_list:
            print(text)
    else:
        print("no such file")
def remv(file_path, this_folder, root_folder):
    found_bool, folder , file, folders_path = find_by_directory(file_path,  this_folder, root_folder )
    folder : Folder
    file : File
    if found_bool == True and file != None:
        folder.rmv(f"{file.get_name()}.{file.get_format()}")
    elif found_bool == True and file == None:
        folders_path[-2].rmv(folders_path[-1].get_name())
        







