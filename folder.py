from file import File
class Folder:
    """
    represents a folder as a class
    
    Attributes :
    folders -> list of folders
    files -> list of files
    name -> folders name

    methodes:
    add_file -> adds a file and sets the first argumant as its name and second argumant as its format
    add_folder -> adds a folder and sets the first argumant as its name

    
    
    
    """
    def __init__(self, name):
        """
        initites the attributes 
        folders, files, name
        """
        self.__folders = []
        self.__files = []
        self.__name = name
    
    def get_name(self):
        """
        returns the folder name
        """
        return self.__name
    
    def add_folder(self, new_folder_name):
        """
        adds a new folder to this directory and sets the name as the new_folder_name

        """
        self.folders.append(Folder(new_folder_name))
    def add_file(self, new_file_name, new_file_format):
        """
        adds a new file to this directory and sets its name as the first argumant and format as the second argumant
        """
        self.folders.append(File(new_file_name,new_file_format))
    
    def print_all_dir(self):
        """
        prints all directories in the specific file
        """
        for folder in self.__folders:
            folder : Folder
            print(folder.get_name(), 'folder')
        for file in self.__files:
            file : File
            print(f'{file.get_name()}.{file.get_format()}')

    def search_folders_by_name(self, folders_name):
        """
        returns a folder as an object 
        """
        for folder in self.__folders:
            folder : Folder
            if folder.get_name() == folders_name:
                return folder
        return None

    def search_files_by_name(self, files_name, files_format):
        """
        returns a file as an object
        """
        for file in self.__files:
            file : File
            if file.get_name() == files_name and file.get_format() == files_format:
                return file
        return None
    
    def print_text_file(self, files_name, files_format):
        """
        prints a text written in a file
        """
        file = self.search_files_by_name(files_name, files_format)
        file : File
        print(file.get_text())
    
    def edit_file(self, files_name, files_format, text):
        """
        rewrite a file with the given text
        """
        file = self.search_files_by_name(files_name, files_format)
        file : File
        file.new_text(text)




    