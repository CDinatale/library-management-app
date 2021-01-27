from datetime import datetime, timedelta

class Book:
    def __init__(self, bookNumber, title, author, category): 
        self.bookNumber = bookNumber
        self.title = title
        self.author = author
        self.category = category
        
    def getDueDate(self):
        dt = datetime.now()
        td = timedelta(days=7)
        my_date = dt + td
        return my_date.strftime("%B %d, %Y")

        
    
