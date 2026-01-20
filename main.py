def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book

    """Reads the content of a book from a text file and returns it as a string."""

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
