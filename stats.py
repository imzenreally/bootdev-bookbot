def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_letter_count(book_text):
    counts = {}
    text_lower = book_text.lower()
    for char in text_lower:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts


