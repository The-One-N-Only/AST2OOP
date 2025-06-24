#2024 23/06/25
#Aarush Alajangi
#Software Engineering Assessment task 2

import os
import datetime

def cls():
    os.system('clear')

def CurrentDay():
    return datetime.now().day

class LibrarySystem:
    def __init__(self):
        self.items_by_title = {}
        self.items_by_ID = {}

    def add_item(self, item):
        self.items_by_title[item.title.lower()] = item
        self.items_by_ID[item.ID] = item

    def get_by_title(self, title):
        if title.lower() not in self.items_by_title:
            return "No item of that name found."
        return self.items_by_title.get(title.lower())
    
    def get_by_ID(self, id):
        if id not in self.items_by_title:
            return "No item of that ID found."
        return self.items_by_ID.get(id)
    
    def borrow_item_by_title(self, title):
        item = self.get_by_title(title)
        if item is str:
            print(self.get_by_title(title))
        elif item.is_available() == False:
            print("This item has been borrowed")
        else:
            item.borrow_item()
            print(f"you have borrowed {self.title}")

    def borrow_item_by_ID(self, id):
        item = self.get_by_ID(id)
        if item is str:
            print(self.get_by_ID(id))
        else:
            item.borrow_item()
            print(f"you have borrowed {self.title}")

    def return_item_by_title(self, title):
        item = self.get_by_title(title)
        if item is str:
            print(self.get_by_title(title))
        else:
            item.return_item()
            print(f"you have returned {self.title}")

    def return_item_by_ID(self, id):
        item = self.get_by_ID(id)
        if item is str:
            print(self.get_by_ID(id))
        else:
            item.return_item()
            print(f"you have returned {self.title}")
    def get_all_borrowed_items(self):
        item = self.available
        if item == False:
            print(f"{self.items_by_title}")
    def get_all_available_items(self):
        print(f"{self.items_by_title}")
    

class LibraryItem:
    def __init__(self, title, item_id, genre, type, author, available = True):
        self.title = title
        self.type = type
        self.item_id = item_id
        self.available = available
        self.genre = genre
        self.type = type
        self.author = author
    
    def is_available(self):
        return self.available

    def display_info(self):
        return f"This is a {self.type} with title {self.title} and genre {self.genre}, {self.available}"

    def borrow_item(self):
        self.available = False

    def return_item(self):
        self.available = True


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, num_pages, available = True):
        super().__init__(self, title, item_id, genre, author, type="Book", available = True)
        self.num_pages = num_pages

    def display_info(self):
        return super().display_info().append(f"{self.num_pages}")


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, genre, issue_number = 1, publication_date = CurrentDay, available = True):
        super().__init__(self, title, item_id, genre, author, type="Magazine", available = True)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def display_info(self):
        return super().display_info().append(f"{self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, author, item_id, genre, duration, director, available = True):
        super().__init__(self, title, item_id, genre, author, type="item", available = True)
        self.duration = duration
        self.director = director

    def display_info(self):
        return super().display_info().append(f"{self.num_pages}")
def main():
#     cls()
#     print(r"""
# ┓ •┓        
# ┃ ┓┣┓┏┓┏┓┏┓┏
# ┗┛┗┗┛┛ ┗┻┛┗┫
#            ┛""") #ascii art: tmplr
# main()

