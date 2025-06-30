class Book:

    def __init__(self, title, author, year):

        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = "available"

    def check_out(self):

        if self.__status == "available":
            self.__status = "checked out"
            return f"The book '{self.__title}' has been checked out."
        else:
            return f"The book '{self.__title}' is not available."

    def return_book(self):

        if self.__status == "checked out":
            self.__status == "available"
            return f"The book '{self.__title}' has been returned."
        else:
            return f"The book '{self.__title}' is not checked out."

    def get_info(self):

        info = (
            f"Title: {self.__title}\n"
            f"Author: {self.__author}\n"
            f"Year: {self.__year}\n"
            f"Status: {self.__status}\n"
        )
        
        return info


    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year
