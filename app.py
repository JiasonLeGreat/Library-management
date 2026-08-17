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
         menu()

        choice = input("Choose an option from 1-5 ").strip()

        if choice == '1':

            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            id = input("Enter unique id: ").strip()
            if title and author and id:
                manager.add_book(title, author, id)
            else:
                print("❌ All fields are required.")

        elif choice == '2':
           
           manager.view_books()

        elif choice == '3':

            id = input("Enter ISBN of the book to borrow: ").strip()
            manager.borrow_book(id)
        
        elif choice == '4':

            id = input("Enter Id of the book to return: ").strip()
            manager.return_book(id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print('Invalid option, pick again')

if __name__ == "__main__":
    main()
