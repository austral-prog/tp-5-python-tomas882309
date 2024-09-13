from typing import List
from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books: List[Book] = []
        self.__users: List[User] = []
        self.__checked_out_books:List[tuple] = []
        self.__checked_in_books:List[tuple] = []

    # Getters
    def get_books(self)->List[Book]:
        return self.__books

    def get_users(self)->List[User]:
        return self.__users

    def get_checked_out_books(self)->List[tuple]:
        return self.__checked_out_books

    def get_checked_in_books(self)->List[tuple]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str)->None:
        for book in self.__books:
            if book.get_isbn() == isbn:
                pass
        lista : Book = Book(isbn, title, author)
        self.__books.append(lista)

    # 1.2 List All Books
    def list_all_books(self)->None:
        for book in self.__books:
            print (book.__str__())

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: str, due_date: str)->str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                for user in self.__users:
                    if user.get_dni() == dni:
                        if book.is_available() == True:
                            self.__checked_out_books.append((isbn, dni, due_date))
                            user.increment_checkouts()
                            book.increment_checkout_num()
                            book.set_available(False)
                            return f"User {dni} checked out book {isbn}"
                        else:
                            return f"Book {isbn} is not available"

                    else:
                        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
            else:
                return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"


    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: str, returned_date: str)->str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                for user in self.__users:
                    if user.get_dni() == dni:
                        if book.is_available() == False:
                            self.__checked_in_books.append((isbn, dni, returned_date))
                            self.__checked_out_books.clear()
                            user.increment_checkins()
                            book.set_available(True)
                            return f"Book {isbn} checked in by user {dni}"
                        else:
                            return f"Book {isbn} is not available"

                    else:
                        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
            else:
                return f"Book {isbn} is not available"

    # Utils
    def add_user(self, dni: str, name: str)->None:
        self.__users.append(User(dni, name))
