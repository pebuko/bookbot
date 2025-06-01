from stats import get_word_count
from stats import text_stats


def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text



def main():
    relpath = "books/frankenstein.txt"
    result = get_book_text(relpath)
    word_count = get_word_count(result)
    print (f"{word_count} words found in the document")
    stats = text_stats(result)
    print(stats)
main()


