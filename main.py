#bookbot
from stats import get_num_words, character_number


def get_book_text():
    with open("/home/bmax/workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = get_book_text()
    new_count = get_num_words(file_contents)
    chars_dict = character_number(file_contents)
    print (f"{new_count} words found in the document")
    print (chars_dict)


main()
