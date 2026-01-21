from stats import get_word_count, get_letter_count

def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    print(f"Found {word_count} total words")
    sorted_items = sorted(
        letter_count.items(),
        key=lambda item: item[1],
        reverse=True
    )
    print(sorted_items)

main()
