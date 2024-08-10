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
        a text variable as a string to write a text 
        """
        self.__name = name
        self.__format = format
        self.__text = ''
    
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
        self.__text = new_text
    
    def get_text(self):
        """
        gives the text written in the file
        """
        return self.__text
    