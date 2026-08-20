from library import LibraryManager
from menu import menu

def main():
    manager = LibraryManager()
    count = 0
    while True:
        if count == 0:        
            print("\nWelcome to the Library Management System")
            menu()
            count += 1
        else:
            print("\nLibrary Managment System")
            menu()

        choice = input("Choose an option from 1-5 ").strip()

        if choice == '1':
            try:
               title = str(input("Enter book title: ").strip())
               author = str(input("Enter book author: ").strip())
               id = int(input("Enter unique id: "))
               if title and author and id:
                    manager.add_book(author, title, id, False)
               else:
                    print("❌ All fields are required.")
            except ValueError:
               print("Invalid Id, numbers only")

        elif choice == '2':
            manager.view_books()

        elif choice == '3':
            try:
                id = int(input("Enter Id of the book to borrow: "))
                manager.borrow_book(id)
            except ValueError:
                print("Invalid Id, numbers only")
        
        elif choice == '4':
            try:
                id = int(input("Enter Id of the book to return: "))
                manager.return_book(id)
            except ValueError:
                print("Invalid Id, numbers only")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print('Invalid option, pick again')

if __name__ == "__main__":
    main()
