from stats import get_num_words
from stats import get_count_chars
from stats import get_sort_chars_list
import sys

def get_book_text(file_path):
    file = open(file_path, "r")
    text = file.read()
    return text

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    book = get_book_text(sys.argv[1])
    
    num_words = get_num_words(book)
    count_chars = get_count_chars(book)
    sort_chars = get_sort_chars_list(count_chars)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sort_chars:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
    
    

    
    return

main()
