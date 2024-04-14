def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_of_dictionaries = [{'letter': k, 'number': v} for k, v in chars_dict.items()]
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for dict_ in list_of_dictionaries:
        letter = dict_["letter"]
        number = dict_["number"]
        print(f"The '{letter}' character was found {number} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["number"]


def get_chars_dict(text):
    lowered_string = text.lower()
    letters = {'a': 0, 'b': 0, 'c': 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0 , "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for char in lowered_string:
        if char in letters:
            letters[char] += 1
    return letters


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
