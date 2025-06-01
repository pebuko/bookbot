def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text

def main():
    relpath = "books/frankenstein.txt"
    result = get_book_text(relpath)
    print(result)


main()


