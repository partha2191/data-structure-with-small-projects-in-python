# Cli Book Store Application
# Version : 1.0.0
# Date : 27-04-2024

def main():
    
    try:
        # initialize book list
        bookList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("theBooksList.txt is not found.")
        print("Starting a new book list...")
        bookList = []

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the author >>> ")
            nPages = input("Enter the number of pages >>> ")
            bookList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            print('Looking up for a book...')
            keyWord = input("Enter the search term >>> ")
            for book in bookList:
                if keyWord in book:
                    print(book)

        elif choice == 3:
            print("Displaying all the books...")
            for i in range(len(bookList)):
                print(bookList[i])

        elif choice == 4:
            print("Quitting Program")
            outfile = open("theBooksList.txt", "w")
            for book in bookList:
                outfile.write("," .join(book) + "\n")
            outfile.close()
        
    print("Program Terminated!")

if __name__ == "__main__":
    main()