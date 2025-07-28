# Software Engineering Assessment Task 2 OOP.
## AST2OOP

------------------------------------------------------------

# Project Overview:
This project is a Python-based Library Management System that demonstrates object-oriented programming concepts like inheritance and polymorphism by managing books, magazines, and DVDs through a command-line interface.

------------------------------------------------------------

# OOP Design
* `Inheritance`
  - `LibraryItem` is the base class for all items 
  - `Book`, `DVD`, and `Magazine` inherit from `LibraryItem`, with their own special attributes like `num_pages` and `duration` etc.
* `Polymorphism`
  - 

------------------------------------------------------------

# Parent Classes
* `LibraryItem`
  - `LibraryItem` is a parent class that the child classes will be based on. It represents a generic library item without specific details, such as the number of pages or duration. This class typically includes common attributes such as `title`, `author`, and `item_id`. It also defines general methods, such as `display_info()` to show item details and `borrow_item`/`return_item()` to manage borrowing status. Child classes inherit these attributes and methods, and can extend or override them to provide specialised behaviour.
# Child Classes
* `Book`
  - `Book` is a child class that inherits from `LibraryItem`. It represents books in the library and adds specific attributes such as `num_pages` to store the number of pages. By inheriting from `LibraryItem`, `Book` automatically gains all the standard functionality (like `display_info()` and `checkout()`), but it can also override these methods to provide book-specific behaviour. This demonstrates inheritance (sharing and extending functionality from a parent class) and polymorphism (allowing methods like `display_info()` to behave differently depending on whether the item is a book, magazine, or DVD).
* `Magazine` 
  - `Magazine` is a child class derived from `LibraryItem`. It represents magazines in the library and introduces attributes specific to magazines, such as `issue_number` and `publication_month`. By inheriting from `LibraryItem`, `Magazine` inherits all the shared functionality, including methods such as `display_info()` and `checkout()`. The class can override these methods to display magazine-specific details or behaviours, illustrating both inheritance (reusing and extending the parent class) and polymorphism (allowing methods to behave differently for magazines compared to other item types). 
* `DVD`
  - `DVD` is a child class that inherits from `LibraryItem`. It represents DVDs in the library and introduces attributes unique to DVDs, such as `duration` (to store the DVD's length in minutes). By inheriting from `LibraryItem`, `DVD` gains all the shared attributes and methods, including `display_info()` and `checkout()`. The `DVD` class can override these methods to display DVD-specific information or exhibit DVD-specific behaviours. This demonstrates inheritance (reusing and extending the parent class's functionality) and polymorphism (allowing methods like `display_info()` to behave differently for DVDs compared to books or magazines).

------------------------------------------------------------

# User instructions
1. Run the main: `main.py`. This will load the Canned Demonstration
2. Follow onscreen instructions

------------------------------------------------------------

# Features
  - Canned Demonstration that runs as soon as program is run: [](Screenshots/rawCannedDemo.png)
  - Arrow Based Navigation [](Screenshots/menuInterface.png)
  - Item Creation based on type [in the file title](Screenshots/itemCreationBook.png)[](Screenshots/itemCreationDVD.png)[](Screenshots/itemCreationMagazine.png)
  - Item borrowing with ID and Title [in the file title](Screenshots/borrowingByID.png)[](Screenshots/borrowingByTitle.png)
  - Item returning with ID and Title [in the file title](Screenshots/returningByID.png)[](Screenshots/returningByTitle.png)
  - Item searching with ID and Title [in the file title](Screenshots/searchingByID.png)[](Screenshots/searchingByTitle.png), and uses closest match algorithm
  - viewing items based on availability [in the file title](Screenshots/viewAll.png)[](Screenshots/viewAvailable.png)[](Screenshots/viewBorrowed.png)

------------------------------------------------------------

# Error Handling
  - Program checks if user input is valid before using it in functions, and advises user as to how they should use the program.