class File:
    """
    represents a file as an object
    Attributes:
    name as its name
    format as its format
    and text as a sting
    methods:


    """
    def __init__(self, name, format) -> None:
        """
        initiates the attributes:
        name, format
        a text variable as a list for each line of the text written in the file 
        """
        self.__name = name
        self.__format = format
        self.__text_list = []
    
    def get_name(self):
        """
        returns the files name
        """
        return self.__name
    
    def get_format(self):
        """
        returns files format
        """
        return self.__format
    
    def new_text(self, new_text):
        """
        deletes past text and adds a new text
        """
        self.__text_list = new_text
    
    def get_text(self):
        """
        gives the text written in the file
        """
        return self.__text_list
    
    def edit_line(self, line, text):
        text_index = line - 1
        self.__text_list[text_index] = text