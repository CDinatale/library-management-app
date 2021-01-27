# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:03:46 2020

@author: corad
"""
from objects import Book

#reads file and saves each line as a Book object in a list
def get_book_list(file):
    books = []
    try:
        with open(file) as f:
            content = f.readlines()
            content = [x.strip() for x in content] #removes whitespace
            for item in content:
                book = item.split(",")
                temp = Book(book[0], book[1], book[2], book[3])
                books.append(temp)
        return books
    except FileNotFoundError:
        print("Could not find the file named" + file)
    except OSError:
        print("File found - error reading file")
    except Exception:
        print("An unexpected Error occured")

def display_main_menu():
    print("\n-----------ABC Library----------\n\nPlease select a choice from the menu below:\n");
    print("1: Search by title \n2: Search by author \n3: Search by category \n4: Exit");

# searches book list for title and returns title if found   
def search_by_title(title):
    master_book_list = get_book_list("master_book_list.txt")
    for book in master_book_list:
        if book.title == title:
            result = book;
            break;
        else:
            result = None;
    return result
            
#searches book list for all books by author, puts objects found in a list and returns list
def search_by_author(author):
    author_list = []
    master_book_list = get_book_list("master_book_list.txt")
    for book in master_book_list:
        if book.author == author:
            author_list.append(book)
    return author_list

#searches book list for all books by category, puts objects found in a list and returns list
def search_by_category(category):
    category_list = []
    master_book_list = get_book_list("master_book_list.txt")
    for book in master_book_list:
        if book.category == category:
            category_list.append(book)
    return category_list
            
            
            
    
    
    
    