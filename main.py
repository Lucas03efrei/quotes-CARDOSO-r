from functions import *
from functions import add_quote


def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Exit")
    print("4. Add a new quote")


def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-3): ")

        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2":
            view_quotes(quotes)
        elif choice == "3":
            print("Good bye...")
        elif choice == "4":
            add_quote(quotes, "quotes.txt")
            break
        else:
            print("Invalid input")
        


if __name__ == "__main__":
    main()

    
