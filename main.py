from stats import *# stats.py



def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        file_text = f.read()
    return file_text



def main():
    relpath = "books/frankenstein.txt"
    result = get_book_text(relpath)
    word_count = get_word_count(result)
    
    stats = text_stats(result)
    stats = sort_stats(stats)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relpath}...")
    print("----------- Word Count ----------")
    print (f"{word_count} words found in the document")
    print("--------- Character Count -------")

main()


