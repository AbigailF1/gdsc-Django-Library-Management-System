from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def borrow_Book_limiter(request, isbn_id):
    student = request.user.student #assuming user model is linked to student 
    if student.borrowed_books.count() >= 3:     
        return render(request, 'some kind of error html.index' ,{'message': 'you can only borrow 3 books at a time'}) #iam not sure about the templates


def book_Track(request, book):
    book = LibraryCatalog.models.Book.objects.get(pk=isbn_id)
    if book.status != 'available':
        return render(request, {"message":"this book"})

def update_book(request, ):
    book.status = 'borrowed'
    book.borrowed_by = student
    book.save()

    Borrowing.models.BorrowedBook.objects.create(book=book, student=student)
# ... (success message and redirect)



def return_book(request, isbn_id):
    book = LibraryCatalog.models.Book.objects.get(pk=isbn_id)
    if book.status == 'borrowed' and book.borrowed_by == request.user.student:
        book.status = 'available'
        book.borrowed_by = None
        book.save()

        Borrowing.models.BorrowedBook.objects.filter(book=book).delete()
        # ... (success message and redirect)
    else:
        # Handle case where book is not borrowed by the student or is not borrowed
        return render(request, 'error.html', {'message': 'There was an error returning this book.'})

