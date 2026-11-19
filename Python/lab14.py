books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {book[3] for book in books}
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("LIBRARY BOOK & CATEGORY MANAGER")

while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\nCurrent Library Catalog (Fixed Records)")
        for i, book in enumerate(books, 1):
            title, author, year, category = book
            print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        print("\nAdd New Book Record")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")
        if title and author and year and category:
            books.append((title, author, year, category))
            library_categories.add(category)
            print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("[ERROR] All fields are required.")

    elif choice == "3":
        print("\nUnique Categories Available in Library (Set)")
        for cat in sorted(library_categories):
            print(f"- {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        print("\nAdd to Student Wishlist")
        req_cat = input("Enter requested category: ")
        student_wishlist.add(req_cat)
        print(f'[SUCCESS] "{req_cat}" added to student wishlist.')

    elif choice == "5":
        print("\nCATEGORY GAP ANALYSIS")
        print(f"Library Holdings (Set): {sorted(list(library_categories))}")
        print(f"Student Wishlist (Set): {sorted(list(student_wishlist))}")
        print(f"\n1. Already in Stock (Intersection &):\n{sorted(list(library_categories & student_wishlist))}")
        print(f"\n2. Purchase Order Needed (Difference -):\n{sorted(list(student_wishlist - library_categories))}")
        print(f"\n3. Full Combined Genre Coverage (Union |):\n{sorted(list(library_categories | student_wishlist))}")

    elif choice == "6":
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
