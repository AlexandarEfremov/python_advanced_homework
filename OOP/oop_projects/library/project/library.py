from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # store the users of the lib
        self.books_available = {}  # info regarding authors: key and books available for each of them: value(list)
        self.rented_books = {}  # keep info regarding the usernames: key and a nested dict {}: value which,
        # will keep info book_name: key and days left before returning: value int

        # {usernames: {book names: days to return}}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in' \
                       f'{data[book_name]} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)

        return f"{user.username} doesn't have this book in his/her records!"