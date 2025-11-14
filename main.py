from stats import get_word_count, get_character_frequency, get_sorted_dict_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    filepath = sys.argv[1]
    # filepath = "./books/frankenstein.txt"
    print("============ BOOKBOT ============")
    
    print(f'Analyzing book found at {filepath}')
    text = get_book_text(filepath)
    
    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")

    character_frequency = get_character_frequency(text)
    sorted_dicts = get_sorted_dict_list(character_frequency)
    for dict in sorted_dicts:
        if dict["char"].isalpha():
            print(f"""{dict["char"]}: {dict["num"]}""")
    print("============= END ===============")
main()
