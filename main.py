def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_count = count_characters(text)
    char_count_sorted = sort_dict(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in the document")
    for count in char_count_sorted:
        if count["char"].isalpha():
            print(f"The {count['char']} character was found {count['num']} times")
    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for c in text:
        try:
            char_count[c.lower()]+= 1 
        except:
            char_count[c.lower()] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    char_list = [{"char" : key, "num": value} for key, value in dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()
