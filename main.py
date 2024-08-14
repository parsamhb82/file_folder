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
yfileedit -> edit a line in the file checklfrtrdf
cat -> file text check
../ -> goes back check
"""

root_folder = Folder('/')
this_folder = root_folder
folders_list = []
folders_list.append(this_folder)

def find_by_directory(directory : str, this_folder : Folder, root_folder : Folder):
    direction_folders = []
    if not directory: 
        current_folder = this_folder
        return True, current_folder, None, []
    elif directory[0] == '/':
        directory = directory[1:]
        current_folder = root_folder
        direction_folders.append(root_folder)
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

def back(folders_list, root_folder):
    if len(folders_list) > 1:
        folders_list.pop()
        current_folder = folders_list[-1]
        return current_folder, folders_list
    print("can't go back from root_folder")
    return root_folder, folders_list



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

def new_folder_file_name(path, this_folder, root_folder, name):
    found_bool, folder , file, folders_path = find_by_directory(path,  this_folder, root_folder)
    if file != None and found_bool :
        file : File
        file.new_name(name)
    elif file == None and found_bool and folder != None:
        folder.new_name(name)
        
def mkfile(path, this_folder, root_folder, file_name, file_format):
    if path != None:
        found_bool, folder , file, folders_path = find_by_directory(path,  this_folder, root_folder )
        if found_bool and folder != None and file == None:
            folder : Folder
            folder.add_file(file_name, file_format)
    else:
        this_folder : Folder
        this_folder.add_file(file_name, file_format)

def mkdir(folder_name, path = None):
    found_bool , folder, file, _ = find_by_directory(path,  this_folder, root_folder )
    if found_bool and folder and file == None and path != None:
        folder.add_folder(folder_name)
    elif found_bool and folder and file == None and path == None:
        this_folder.add_folder(folder_name)
    else:
        print("no such directory")

def move(source_path: str, destination_path: str, this_folder : Folder, root_folder):
    if '.' in source_path.split('/')[-1]:
        move_file_to_file(source_path, destination_path, this_folder, root_folder)
    else:
        move_folder_to_folder(source_path, destination_path, this_folder, root_folder)

def copy(source_path: str, destination_path: str, this_folder : Folder, root_folder):
    if '.' in source_path.split('/')[-1]:
        copy_file_to_file(source_path , destination_path , this_folder , root_folder)
    else:
        copy_folder_to_folder(source_path , destination_path , this_folder , root_folder)
def new_file_text(path, this_folder, root_folder):
    found, folder, file, _ = find_by_directory(path, this_folder, root_folder)
    if found and file != None:
        text = []
        print("enter the lines (/end/ means done) ")
        while(True):
            inp = input()
            text.append(inp)
            if inp == '/end/':
                break
        file.new_text(text)
    else:
        print("file was not found")
    
def app_file(path, this_folder, root_folder):
    found, folder, file, _ = find_by_directory(path, this_folder, root_folder)
    if found and file != None:
        text = []
        print("enter the lines (/end/ means done) ")
        while(True):
            inp = input()
            text.append(inp)
            if inp == '/end/':
                break
        files_text = file.get_text()
        del files_text[-1]
        files_text = files_text + text
        file.new_text(files_text)
    else:
        print("file was not found")

def edit_line(path, this_folder, root_folder, line, text):
    found, folder, file, _ = find_by_directory(path, this_folder, root_folder)
    if found and file != None:
        if line >= len(file.get_text()):
            print('no such line in file')
            return
        file.edit_line(line, text)
        return



            





while True:
   for folder in folders_list:
       folder : Folder
       print(folder.get_name(),end = "/")
   command = input("")
   
   if command.startswith('cd '):
        directory = command[3:]
        this_folder, folders_list = cd(directory, this_folder, folders_list, root_folder)


   elif command == '../':
        this_folder, folders_list = back(folders_list, root_folder)


   elif command.startswith('cat '):
        directory  = command[4:]
        cat(directory, this_folder, root_folder)

   elif command.startswith('mv '):
        parts = command.split()
        if len(parts) == 3:
            _ , source_path, destination_path  = parts
            move(source_path , destination_path , this_folder , root_folder)
        else:
           print("Invalid mv command format. Use: mv source_path destination_path")

   elif command.startswith("cp "):
        parts = command.split()
        if len(parts) == 3:
            _ , source_path, destination_path  = parts
            copy(source_path , destination_path , this_folder , root_folder)
        else:
           print("Invalid cp command format. Use: cp source_path destination_path")
   elif command.startswith("mkdir "):
        parts = command.split()
        path = None
        if len(parts) == 3:
           path = parts[1]
           name = parts[2]
           mkdir(name, path)
        else:
            name = parts[1]
            mkdir(name, path)

   elif command.startswith('rm '):
       parts = command.split()
       if len(parts) == 2:
           path = parts[1]
           remv(path, this_folder, root_folder)
       else:
          
           print("Invalid rm command format. Use: rm path")
   elif command == 'ls':
            this_folder.print_all_dir()

   elif command.startswith('mkfile'):
       parts = command.split()
       if len(parts) == 2:
          path = None
          file_name = parts[1].split('.')[0]
          file_format = parts[1].split('.')[1]
          mkfile(path, this_folder, root_folder, file_name, file_format)
       elif len(parts) == 3:
          path = parts[1]
          file_name = parts[2].split('.')[0]
          file_format = parts[2].split('.')[1]
          mkfile(path, this_folder, root_folder, file_name, file_format)
       else:
          print("wrong format")
   elif command.startswith("nwfile "):
        parts = command.split()
        path = parts[1]
        new_file_text(path, this_folder, root_folder)
   elif command.startswith("appfile"):
        parts = command.split()
        path = parts[1]
        app_file(path, this_folder, root_folder)
   elif command.startswith("editline"):
       parts = command.split()
       path = parts[1]
       line = int(parts[2])
       text = parts[3]
       edit_line(path, this_folder, root_folder, line, text)


    
           
       
        

           
       





        





