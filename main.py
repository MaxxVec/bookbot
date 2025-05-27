#bookbot

def get_book_text():
    with open("/home/bmax/workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count():
    words = get_book_text()
    count= len(words.split())
    print (f"{count} words found in the document")

def main():
    word_count()
    


main()
