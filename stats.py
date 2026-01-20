def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_letter_count(book_text):
    words = book_text.split()
    letters = words.split()
    print(letters)
