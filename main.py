import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import get_char_num
from stats import sort_dict

def get_book_text(file_path):
    """
    This function collects a file path,, read its contents and returns it contents as a string
    """
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    num_words = get_num_words(file_contents)
    chars_num = get_char_num(file_contents)
    list_of_dicts = sort_dict(chars_num)

    #Report Printing Section
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list_of_dicts:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")
    #print(f"{num_words} words found in the document")
    #print(chars_num)
    #print(list_of_dicts)

main()