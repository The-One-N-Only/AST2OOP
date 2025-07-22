#2024 23/06/25
#Aarush Alajangi
#Software Engineering Assessment task 2

import json
import os
import datetime
import time
import readchar
from colorama import Fore, Style, init 

def cls():
    os.system('clear')
def CurrentDay():
    return datetime.date.today()

class LibrarySystem:
    def __init__(self):
        self.items_by_title = {}
        self.items_by_ID = {}
        self.items = []
        self.previousActions = []

    def add_item(self, item):
        if item.title.lower() not in self.items_by_title:
            self.items_by_title[item.title.lower()] = item
            self.items_by_ID[item.item_id] = item
            self.items.append(item)
            print(f"Item {item.title} added successfully.")
            self.previousActions.append(f"Added item: {item.title}")
        else:
            print(f"Item with title {item.title} already exists in the library.")
        

    def get_by_title(self, title):
        if title.lower() not in self.items_by_title:
            return "No item of that name found."
        else:
            return self.items_by_title.get(title.lower())
    
    def get_by_ID(self, id):
        if id not in self.items_by_ID:
            return "No item of that ID found."
        else:
            return self.items_by_ID.get(id)
    
    def borrow_item_by_title(self, title):
        item = self.get_by_title(title)
        if isinstance(item, str):
            print(item)
        elif item.is_available() is False:
            print("This item has been borrowed")
        else:
            item.borrow_item()
            print(f"you have borrowed {title}")
            self.previousActions.append(f"Borrowed item: {title}")

    def borrow_item_by_ID(self, id):
        item = self.get_by_ID(id)
        if isinstance(item, str):
            print(item)
        else:
            item.borrow_item()
            print(f"you have borrowed {item.title}")
            self.previousActions.append(f"Borrowed item: {item.title}")
    
    def return_item_by_title(self, title):
        item = self.get_by_title(title)
        if isinstance(item, str):
            print(item)
        else:
            item.return_item()
            print(f"You have returned {item.title}.")
            self.previousActions.append(f"Returned item: {item.title}")
        
    def return_item_by_ID(self, id):
        item = self.get_by_ID(id)
        if isinstance(item, str):
            print(item)
        else:
            item.return_item()
            print(f"You have returned {item.title}.")
            self.previousActions.append(f"Returned item: {item.title}")

    def get_all_borrowed_items(self):
        borrowed_list = []
        for item in self.items_by_title.values():
            if not item.available:
                borrowed_list.append(item)
        if not borrowed_list:
            print("No items are currently borrowed.")
        return borrowed_list

    def get_all_available_items(self):
        available_list = []
        for item in self.items_by_title.values():
            if item.available:
                available_list.append(item)
        if not available_list:
            print("No items are currently available.")
        return available_list

    def get_all_items(self):
        if not self.items:
            print("No items in the library.")
            return []
        return self.items

    def print_by_title(self, title):
        result = self.get_by_title(title)
        if isinstance(result, str):
            print(result)
            time.sleep(1)  # Wait for 2 seconds before clearing the screen
        else:
            print(result.display_info())

    def print_by_ID(self, id):
        result = self.get_by_ID(id)
        if isinstance(result, str):
            print(result)
        else:
            result.display_info()
        
    

class LibraryItem:
    def __init__(self, title, item_id, genre, author, type, available = True):
        self.title = title
        self.type = type
        self.item_id = item_id
        self.available = available
        self.genre = genre
        self.author = author
    
    def is_available(self):
        return self.available

    def display_info(self):
        return f"\n{self.title} ({self.type})\nID: {self.item_id}\nGenre: {self.genre}\nAuthor: {self.author}\nAvailable: {'Yes' if self.available else 'No'}"

    def borrow_item(self):
        self.available = False

    def return_item(self):
        self.available = True
    
    def __str__(self):
        line = ""
        # Print attributes in the order they are defined in the class
        attrs = ["title", "type", "item_id", "available", "genre", "author"]
        # Add any extra attributes that may be defined in subclasses
        extra_attrs = [attr for attr in self.__dict__ if attr not in attrs]
        for attr in attrs + extra_attrs:
            values = []
            for attr in attrs + extra_attrs:
                value = getattr(self, attr, None)
                values.append(f"{attr}: {value}")
            line = ", ".join(values)
        return line


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, num_pages, available = True):
        super().__init__(title, item_id, genre, author, type="Book", available = True)
        self.num_pages = num_pages

    def display_info(self):
        return super().display_info() + f"\nNumber of Pages: {self.num_pages}\n"


class Magazine(LibraryItem): #Magazine item, with issue number and publication date (set to today by default)
    def __init__(self, title, author, item_id, genre, issue_number = 1, publication_date = CurrentDay(), available = True):
        super().__init__(title, item_id, genre, author, type="Magazine", available = True)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def display_info(self):
        return super().display_info() + f"\nIssue Number: {self.issue_number}\nPublication Date: {self.publication_date}\n"


class DVD(LibraryItem): #DVD item, with duration and director
    def __init__(self, title, author, item_id, genre, duration, director, available = True):
        super().__init__(title, item_id, genre, author, type="item", available = True)
        self.duration = duration
        self.director = director

    def display_info(self):
        return super().display_info() + f"\nDuration: {self.duration} seconds\nDirector: {self.director}\n"



def printInLine(list, listIndex):
    lines = [text.split('\n') for text in list]
    max_lines = max(len(text.split('\n')) for text in list)
    for line_index in range(max_lines):
        for i, text in enumerate(list):
            line_parts = text.split('\n')
            if line_index < len(line_parts):
                part = line_parts[line_index]
                if i == listIndex:
                    print(Fore.BLUE + part + Style.RESET_ALL, end='  ')
                else:
                    print(part, end='  ')
            else:
                print(" " * len(line_parts[0]), end='  ')
        print()

def Highlight(options, optionsIndex, menuTitle, previousActions = None):
        def print_menuOpt():
            cls()  # Clear the screen
            print(menuTitle)
            printInLine(options, optionsIndex)  # Print the text blocks side by side
            printPreviousActions(previousActions)  # Print previous actions if any
            return
        print_menuOpt()
        return

def printPreviousActions(previousActions):
    if not previousActions:
        return
    print("Previous Actions:")
    for action in previousActions[-10:]:
        print(action)




mainTitle = """
                     __       __  .______   .______          ___      .______     ____    ____
                    |  |     |  | |   _  \  |   _  \        /   \     |   _  \    \   \  /   /
                    |  |     |  | |  |_)  | |  |_)  |      /  ^  \    |  |_)  |    \   \/   / 
                    |  |     |  | |   _  <  |      /      /  /_\  \   |      /      \_    _/  
                    |  `----.|  | |  |_)  | |  |\  \----./  _____  \  |  |\  \----.   |  |    
                    |_______||__| |______/  | _| `._____/__/     \__\ | _| `._____|   |__|    


"""

mainOpt = [
    "                     ╔═══════════╗\n                     ║Create Item║\n                     ╚═══════════╝",
    "╔═══════════╗\n║Borrow Item║\n╚═══════════╝",
    "╔═══════════╗\n║Return Item║\n╚═══════════╝",
    "╔═══════════╗\n║Search Item║\n╚═══════════╝",
    "╔═══════════╗\n║ View Item ║\n╚═══════════╝"
]

viewTitle = """┓┏•       ┳┳┓   ┓   
┃┃┓┏┓┓┏┏  ┃┃┃┏┓┏┫┏┓•
┗┛┗┗ ┗┻┛  ┛ ┗┗┛┗┻┗ •
                    """#ascii art: tmplr

viewOpt = [
    "                     ╔═════════╗\n                     ║ Borrowed║\n                     ╚═════════╝",
    "╔═════════╗\n║Available║\n╚═════════╝",
    "╔═════════╗\n║   All   ║\n╚═════════╝",
]

searchTitle = """┏┓       ┓   ┳┳┓   ┓   
┗┓┏┓┏┓┏┓┏┣┓  ┃┃┃┏┓┏┫┏┓•
┗┛┗ ┗┻┛ ┗┛┗  ┛ ┗┗┛┗┻┗ •
                       """

searchOpt = [
    "                     ╔═════════╗\n                     ║By Title:║\n                     ╚═════════╝",
    "╔═════════╗\n║ By ID:  ║\n╚═════════╝",
]

def cannedDemonstration(ArdenSystem):
    libraryItem1 = Book("Harry Potter", "J.K. Rowling", "000001", "Fantasy", 500)
    ArdenSystem.add_item(libraryItem1)
    libraryItem2 = Magazine("Time", "Time Inc.", "000002", "News", 1, CurrentDay())
    ArdenSystem.add_item(libraryItem2)
    ArdenSystem.borrow_item_by_title("Harry Potter")  # Borrowing Harry Potter to test borrowing functionality
    ArdenSystem.borrow_item_by_ID("000002")  # Borrowing Time magazine to test
    libraryItem3 = DVD("Inception", "Christopher Nolan", "000003", "Sci-Fi", 148, "Christopher Nolan")
    ArdenSystem.add_item(libraryItem3)
    libraryItem4 = Book("The Hobbit", "J.R.R. Tolkien", "000004", "Fantasy", 310)
    ArdenSystem.add_item(libraryItem4)
    libraryItem5 = Magazine("National Geographic", "National Geographic Society", "000005", "Science", 2, CurrentDay())
    ArdenSystem.add_item(libraryItem5)
    libraryItem6 = DVD("The Matrix", "Lana Wachowski", "000006", "Sci-Fi", 136, "Lana Wachowski")
    ArdenSystem.add_item(libraryItem6)
    ArdenSystem.borrow_item_by_title("The Matrix")
    ArdenSystem.return_item_by_title("The Matrix")

def main():
    ArdenSystem = LibrarySystem()  # Create an instance of the LibrarySystem
    cannedDemonstration(ArdenSystem)
    raw_id = 7  # Start with an ID of 7, assuming IDs 1-6 are already taken

    while True:
        action = mainMenu(ArdenSystem.previousActions)  # Get the action from the main menu
        if action == "c":
            cls()
            print("""┏┓ ┓ ┓  ┳       
┣┫┏┫┏┫  ┃╋┏┓┏┳┓•
┛┗┗┻┗┻  ┻┗┗ ┛┗┗•
                """)
            title = input("Title: ")
            item_id = str('000000'[len(str(raw_id)):] + str(raw_id))
            raw_id += 1
            genre = input("Genre: ")
            author = input("Author/Publisher/Producer: ")
            while True:
                type = input("Item Type: ")
                match type.lower():
                    case "book":
                        while True:
                            try:
                                num_pages = int(input("Number of pages:"))
                            except ValueError:
                                print("Try again")                            
                            libraryitem = Book(title, author, item_id, genre, num_pages)
                            ArdenSystem.add_item(libraryitem)
                            break
                        break
                    case "magazine":
                        issue_number = int(input("Issue number: "))
                        publication_date = input("Date published (DD/MM/YYYY): ")
                        if publication_date == '':
                            publication_date = CurrentDay()
                            break
                        try:
                            publication_date = datetime.datetime.strptime(publication_date, "%d/%m/%Y").date()
                            break
                        except ValueError:
                            print("Invalid date format. Please use DD/MM/YYYY.")
                        libraryitem = Magazine(title, author, item_id, genre, issue_number, publication_date)
                        ArdenSystem.add_item(libraryitem)
                        break
                    case "dvd":
                        director = input("Director: ")
                        durationstr = input("Duration (HH:MM:SS): ")
                        duration = durationstr.split(":")
                        duration = int(duration[0]) * 3600 + int(duration[1]) * 60 + int(duration[2])
                        libraryitem = DVD(title, author, item_id, genre, duration, director)
                        ArdenSystem.add_item(libraryitem)
                        break
                    case _:
                        print("Invalid item type. Please try again.")
            readchar.readkey()  # Wait for a key press before continuing
        elif action == "b":
            match searchMenu():
                case "t":
                    title = input("Title to borrow: ")
                    ArdenSystem.borrow_item_by_title(title)
                    readchar.readkey()
                case "i":
                    id_num = int(input("ID Number: "))
                    ArdenSystem.borrow_item_by_ID(id_num)
        elif action == "r":
            match searchMenu():
                case "t":
                    title = input("Title to return: ")
                    item = ArdenSystem.get_by_title(title)
                    if isinstance(item, str):
                        print(item)
                    else:
                        item.return_item()
                        print(f"You have returned {item.title}.")
                case "i":
                    id_num = int(input("ID Number: "))
                    item = ArdenSystem.get_by_ID(id_num)
                    if isinstance(item, str):
                        print(item)
                    else:
                        item.return_item()
                        print(f"You have returned {item.title}.")
                        readchar.readkey()  # Wait for a key press before continuing
        elif action == "s":
            match searchMenu():
                case "t":
                    title = input("Title to view: ")
                    ArdenSystem.print_by_title(title)
                    readchar.readkey()  
                case "i":
                    id_num = input("ID Number: ")
                    ArdenSystem.print_by_ID(id_num)
                    readchar.readkey()  
        elif action == "v":
            match viewMenu():
                case "b":
                    items = ArdenSystem.get_all_borrowed_items()
                case "a":
                    items = ArdenSystem.get_all_available_items()
                case "aa":
                    items = ArdenSystem.get_all_items()
            for i in items:
                print(i)
                time.sleep(0.2)
            readchar.readkey()

def mainMenu(previousActions):
    index = 0
    Highlight(mainOpt, index, mainTitle, previousActions)

    while True:
        key = readchar.readkey()  # Read a single key press
        if key == readchar.key.LEFT:  # left arrow key
            index = (index - 1) % len(mainOpt)  # Move selection up
        elif key == readchar.key.RIGHT:  # right arrow key
            index = (index + 1) % len(mainOpt)  # Move selection down
        elif key == readchar.key.ENTER or key == readchar.key.DOWN:
            if index == 0:
                return "c"
            elif index == 1:    
                return "b"
            elif index == 2:
                return "r"
            elif index == 3:
                return "s"
            elif index == 4:
                return "v"

        Highlight(mainOpt, index, mainTitle, previousActions)  # Update the highlighted option

def searchMenu():
    index = 0
    Highlight(searchOpt, index, searchTitle)

    while True:
        key = readchar.readkey()  # Read a single key press
        if key == readchar.key.LEFT:  # left arrow key
            index = (index - 1) % len(searchOpt)  # Move selection up
        elif key == readchar.key.RIGHT:  # right arrow key
            index = (index + 1) % len(searchOpt)  # Move selection down
        elif key == readchar.key.ENTER or key == readchar.key.DOWN:
            if index == 0:
                return "t"
            elif index == 1:
                return "i"
        Highlight(searchOpt, index, searchTitle)

def viewMenu():
    index = 0
    Highlight(viewOpt, index, viewTitle)

    while True:
        key = readchar.readkey()  # Read a single key press
        if key == readchar.key.LEFT:  # left arrow key
            index = (index - 1) % len(viewOpt)  # Move selection up
        elif key == readchar.key.RIGHT:  # right arrow key
            index = (index + 1) % len(viewOpt)  # Move selection down
        elif key == readchar.key.ENTER or key == readchar.key.DOWN:
            if index == 0:
                return "b"
            elif index == 1:
                return "a"
            elif index == 2:
                return "aa"
        Highlight(viewOpt, index, viewTitle)


main()


