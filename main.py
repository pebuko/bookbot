def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    relpath = "books/frankenstein.txt"
    result = get_book_text(relpath)
    word_count = get_word_count(result)
    print (f"{word_count} words found in the document")

main()


