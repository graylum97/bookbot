import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_count = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)
    chars_sorted = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_count, chars_sorted)


def get_book_text(filepath):
    with open(filepath) as t:
        return t.read()

def print_report(book_path, char_count, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {char_count} total words")
    print("--------- Character Count -------")
    
    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    

main()