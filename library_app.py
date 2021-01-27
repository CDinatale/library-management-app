# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:39:46 2020

@author: corad
"""
from functions import *
from objects import Book

def main():
    receipt_list = []
    
    while True:
        display_main_menu()        
        command = input("\nEnter your command here: ")
        print("\n-------------------------------------")
        
        #searches data by book title and gives option to add results to receipt list
        if command == "1": 
            title= input("Please enter the name of the book: ")
            book = search_by_title(title)
            if book != None:
                print("\n-----------RESULTS-------------")
                print("\n" + "Title: " + book.title + "\n" + "Author: " + book.author + "\n")
                print("-------------------------------")
                answer= input("Would you like to rent this book? Enter Y or N:  ")
                if answer.lower() == 'y':
                    receipt_list.append(book)
                    print("\n-------------------------------")
                    print ("\n" + book.title + " has been added to your cart!")
                    print("\n-------------------------------")
                    choice = input("Would you like to search for other books? Enter Y or N:  ")
                    if choice.lower() == "y":
                        continue
                    else:
                        break
                else:
                    break
            else:
                print("\n-------------------------------")
                print("\nThe title was not found! Please try again.")
                
        #searches data by author and gives option to add results to receipt list       
        elif command == "2": 
            author= input("Please enter the name of the author: ")
            book_list = search_by_author(author)
            if len(book_list) != 0:
                print("\n-----------RESULTS-------------")
                for book in book_list:
                    print("\n" + book.bookNumber + ":" + " Title: " + book.title + "\n" + "Author: " + book.author + "\n")
                print("-------------------------------")
                answer= input("If you would like to rent one of these books, please enter the book number otherwise enter N:  ")
                for book in book_list:
                    if(book.bookNumber == answer):
                        receipt_list.append(book)
                        print("\n-------------------------------")
                        print ("\n" + book.title + " has been added to your cart!")
                        print("\n-------------------------------")
                choice = input("\nWould you like to search for other books? Enter Y or N:  ")
                if choice.lower() == "y":
                    continue;
                else:
                    break;
            else:
                print("\n-------------------------------")
                print("\nThe author was not found! Please try again.")
                
        #searches data by category and gives option to add results to receipt list        
        elif command == "3": 
            category= input("Please enter the book category: ")
            book_list = search_by_category(category)
            if len(book_list) != 0:
                print("\n-----------RESULTS-------------")
                for book in book_list:
                    print("\n" + book.bookNumber + ":" + " Title: " + book.title + "\n" + "Author: " + book.author + "\n")
                print("\n-------------------------------")
                answer= input("If you would like to rent one of these books, please enter the book number otherwise enter N:  ")
                for book in book_list:
                    if(book.bookNumber == answer):
                        receipt_list.append(book)
                        print("\n-------------------------------")
                        print ("\n" + book.title + " has been added to your cart!")
                        print("\n-------------------------------")
                choice = input("\nWould you like to search for other books? Enter Y or N:  ")
                if choice.lower() == "y":
                    continue;
                else:
                    break;
            else:
                print("\n-------------------------------")
                print("\nThe category was not found! Please try again.")  
                
        # exits loop to generate receipt       
        elif command == "4":
            break;
            
        # generates error message if command is not valid
        else:
            print("\nNot a valid command. Please try again.\n")
            continue
    #generates receipt with list of books and due date
    print("\n----------YOUR RECEIPT----------")
    for book in receipt_list:
        print("\n" + "Title: " + book.title + "\n" + "Author: " + book.author + "\n" 
              + "Due Date: " + "{0}".format(book.getDueDate()) + "\n")
    print("\n-------------------------------")
        
    print("\nThank you for choosing ABC Library. Please come again.")
    

if __name__ == "__main__":
    main()

