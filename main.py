import sys
from stats import string_to_numbers, text_to_characters, sorted_dictonary

def get_book_text(text):
    with open(text) as r:
        file_contents = r.read()
    return file_contents

def print_report(path, numbers, dictionaries):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {numbers} total words")
    print("--------- Character Count -------")

    for dictionary in dictionaries:
        char = dictionary['char']
        count = dictionary['count']
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)

    numbers = string_to_numbers(file_contents)
    characters = text_to_characters(file_contents)
    dictonaries = sorted_dictonary(characters)
    print_report(book_path, numbers, dictonaries)

main()