import os
import time

name = "Shashank Rawat"
sap_id = "500122795"
print("Name:", name, "SAP ID:", sap_id)

class Library:
    Library_Name = "SK_Library"
    Name = " "

    @staticmethod
    def Add_Book():
        print("Existing books:")
        with open("Library.txt", "r") as f:
            existing_books = [line.strip() for line in f if line.strip()]
            for book in existing_books:
                print(book)

        print("To add a book, please enter the book name followed by ~ and then the index, and the author's name in quotes.")
        print("For example: 'Harry Potter~1 \"J.K. Rowling\"'")
        with open("Library.txt", "a") as cout:
            while True:
                book_info = input("Enter book name, index, and author's name (in the format 'book_name~index \"Author's name\"'): ")
                book_info_parts = book_info.split("~")
                if len(book_info_parts) == 2:
                    book_name = book_info_parts[0]
                    book_index = book_info_parts[1].split()[0]  # Extracting the index
                    # Check if the ID already exists
                    if any(book_name in book for book in existing_books):
                        print("A book with this name already exists. Please choose a different name.")
                        continue  # Ask user to enter details again
                    cout.write(f"{book_info}\n")
                    break  # Exit loop if input is valid
                else:
                    print("Invalid input! Please enter book name and index separated by ~.")

    @staticmethod
    def View():
        print("Existing books:")
        with open("Library.txt", "r") as f:
            existing_books = [line.strip() for line in f if line.strip()]
            for book in existing_books:
                print(book)

    @staticmethod
    def Search():
        print("Available book IDs:")
        with open("Library.txt", "r") as f:
            existing_books = [line.strip() for line in f if line.strip()]
            print(existing_books)
        with open("Library.txt", "r") as cin:
            inpu = input("Enter book name to search: ")
            found = False
            for line in cin:
                val = line.strip()
                if inpu in val:
                    print(f"Book found: {val}")
                    found = True
                    break
            if not found:
                print("Book not found.")

    @staticmethod
    def delete():
        cin = open("Library.txt", "r")
        cout = open("temp.txt", "a")
        inpu = input("Enter book name to delete: ")
        try:
            for line in cin:
                val = line.strip()
                if inpu not in val:
                    cout.write(line)
        except ValueError:
            print("Invalid book format in the file.")

        cout.close()
        cin.close()
        os.remove("Library.txt")
        os.rename("temp.txt", "Library.txt")

    @staticmethod
    def update():
        print("To update a book, please enter the new book name followed by ~ and then the new index, and the new author's name in quotes.")
        print("For example: 'New Book~5 \"New Author\"'")

        cin = open("Library.txt", "r")
        cout = open("temp.txt", "w")
        inpu = input("Enter book name to update: ")
        updated = False
        for line in cin:
            val = line.strip()
            if inpu not in val:
                cout.write(line)
            else:
                new_info = input(f"Enter the updated information for '{val}' (in the format 'book_name~index \"Author's name\"'): ")
                cout.write(new_info + "\n")
                updated = True

        if updated:
            os.remove("Library.txt")
            os.rename("temp.txt", "Library.txt")
        else:
            os.remove("temp.txt")
            print("Book not found.")

    @staticmethod
    def lend():
        lending_cost = 50  # Fixed cost for lending each book

        # Read book information from Library.txt
        with open("Library.txt", "r") as library_file:
            books = [line.strip().split("~") for line in library_file if line.strip()]

        print("Contents of books:", books)  # Debug print

        # Split the index from the author's name and remove the quotes around the author's name
        for book in books:
            index_author = book[1].split()
            book[1] = index_author[0]
            book.append(" ".join(index_author[1:])[1:-1])  # Remove the quotes around the author's name

        # Display available books with their IDs and lending cost
        print("Available books:")
        for book_id, book_info in enumerate(books, start=1):
            print(f"ID: {book_id}, Book: {book_info[0]}, Author: {book_info[2]}, Lending Cost: Rs. {lending_cost}")

        try:
            # Prompt user to select a book by its ID
            book_id_to_lend = int(input("Enter book ID number to lend: "))

            # Get the selected book information
            selected_book = books[book_id_to_lend - 1]
            print("Selected book:", selected_book[0])

            # Prompt for lender's name
            lender_name = input("Please enter your name: ")

            # Calculate total lending cost
            total_cost = lending_cost

            # Write lending information to Lend.txt
            with open("Lend.txt", "a") as lend_file:
                lend_file.write(f"{selected_book[0]}~{lender_name}~{total_cost}\n")

            print("Book lent successfully!")

            # Remove the lent book from the library
            books.pop(book_id_to_lend - 1)

            # Update Library.txt with remaining books
            with open("Library.txt", "w") as library_file:
                for book_info in books:
                    library_file.write(f"{book_info[0]}~{book_info[1]} \"{book_info[2]}\"\n")

        except (IndexError, ValueError):
            print("Invalid book ID!")

    @staticmethod
    def return_book():
        # Implementation of returning a book
        pass

if __name__ == '__main__':
    Obj = Library()
    menu = True
    print("\033[34m\033[01m\t\t\t\t\t\t\t\t\t\t\t\t*****************Library Management System*****************")
    while menu:
        print("\033[01m\033[33mPlease Enter 1 for Manager ")
        print("Please Enter 2 for Customer")
        print("Please Enter 3 for Exit   ")
        while True:
            try:
                user = input("Please enter your choice: ")
                if user.strip():  # Check if the input is not empty
                    user = int(user)  # Convert input to an integer
                    break
                else:
                    print("Input cannot be empty. Please enter a valid integer.")
            except ValueError:
             print("Invalid input! Please enter a valid integer.")

        if user == 1:
            passs = True
            while passs:
                pas = int(input("Please Enter Your Password\n"))
                print("\033[31mLoading <", end="")
                for i in range(20):
                    print("|", end="")
                    time.sleep(0.25)
                print(">Processing....\n\n")

                if pas == 1234:
                    GotoM = True
                    while GotoM:
                        print("\033[35mPlease Enter 1 For Add    Books")
                        print("Please Enter 2 For View   Books")
                        print("Please Enter 3 For Search Books")
                        print("Please Enter 4 For Delete Books")
                        print("Please Enter 5 For Update Books")
                        man = int(input())
                        if man == 1:
                            Obj.Add_Book()
                            GotoM = False
                        elif man == 2:
                            Obj.View()
                            GotoM = False
                        elif man == 3:
                            Obj.Search()
                            GotoM = False
                        elif man == 4:
                            Obj.delete()
                            GotoM = False
                        elif man == 5:
                            Obj.update()
                            GotoM = False
                        else:
                            print("Wrong Key ")
                    pass_attempt = 3
                else:
                    print("Incorrect password. Please try again.")
                    pass_attempt += 1
            if pass_attempt == 3:
                print("You've exceeded the maximum number of password attempts.")

        elif user == 2:
            cu = True
            while cu:
                print("\033[35mPress 1 Lend   Book")
                print("Press 2 Return Book")
                cus = int(input())
                if cus == 1:
                    Obj.lend()
                    cu = False
                elif cus == 2:
                    Obj.return_book()
                    cu = False
                else:
                    print("Wrong Key", end=" ")
                    os.system("PAUSE")
        elif user == 3:
            menu = False
        else:
            print("Wrong Key", end=" ")
            os.system("PAUSE")
