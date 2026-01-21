from stats import get_word_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]



def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book

def main():
    from stats import get_letter_count
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in letter_count:
        print(f"{letter}: {count}")


main()
