def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book
def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")

main()
