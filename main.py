def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text
relpath = "books/frankenstein.txt"
def main(relpath):
    get_book_text(relpath)
    print(relpath)
main()


