

# ****wnat to not count with include in 'no of item' when cumtomer worng input*****

# NO. 02  **Library**    

class Library:
    def __init__(self,listofbook):
        self.books = listofbook

    def displayAvailableBook(self):
        print("\n")
        print("Book present in this library are : ")
        for books in self.books:
            print("  * " + books)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"you have been issued book {bookname} pleas keet it safe and return with in 30 days\n")
            self.books.remove(bookname)
            return True
        else:
            print("sorry this book either not available or has been already issued to someone else. please wait until the book is avialable\n")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for ruturning book!  hope you enjoyed reading it")

class Student:
    def requestBook(self):
        self.book = input("enter the name of book which you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Entr the name of book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Django", "pandas", "numpy", "python"])
    # centralLibrary.displayAvailableBook()
    Studentinput = Student()

    while True:
        welcomeMsg = ''' ========= Welcome to CENTRAL LIBRARY =========
        pelase chooose an option:
        1. List all book
        2. Request book
        3. Add/Return book
        4. Exit the Library'''
        print(welcomeMsg)
        try:
            a = int(input("Enter a choice: "))        
            if a == 1:
                centralLibrary.displayAvailableBook()
            elif a == 2:
                centralLibrary.borrowBook(Studentinput.requestBook())
            elif a == 3:
                centralLibrary.returnBook(Studentinput.returnBook())
            elif a == 4:
                print("Thanks for choosing CENTRAL LIBRARY, Have a goood day! ")
                exit()
                break
            else:
                print("Invalid choice! ")
        except Exception as i:
            print(f"please enter valid no.{i} ")