import sys
from stats import count_words, character_count_map,chars_dict_to_sorted_list, print_report

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def __main__():
    print(sys.argv)

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)

    word_count = count_words(book_text)

    char_map = character_count_map(book_text)

    sortedList = chars_dict_to_sorted_list(char_map)

    print_report(path,word_count, sortedList)

if __name__ == "__main__":
    __main__()
