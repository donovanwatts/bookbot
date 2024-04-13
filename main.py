def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")


def get_num_letters(text):
    lowered_string = text.lower()
    letters = {'a': 0, 'b': 0, 'c': 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0 , "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for char in lowered_string:
        if char in letters:
            letters[char] += 1
    print(letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
