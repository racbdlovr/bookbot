
import sys
from stats import get_num_words, get_char_count, get_sorted_chars

# This creates the Function "get_book_text" and makes "filepath" a parameter to pass any valid path to.
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

# This main function will orchastrate the core tasks of the program
def main():
    book_path = sys.argv[1]   # defines a variable called "book_path" and sets it to the location of the text file. So the program can find it
    book_text = get_book_text(book_path)  # calls the function "get_book_text()" and passes in the file path. It opens the file, reads its contents, and returns the whole book as a string. The result is stored in "book_text" 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    num_words = get_num_words(book_text)  #  uses the function "count_words()" to calculate how many words are in the string "book_text". The function breaks the string into a list of words and returns how many items are in the list. The result is stored in "num_words" 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") # prints out the final message showing the total word count, with {num_words} filled in using an f-string for formatting

    char_counts = get_char_count(book_text)
    sorted_chars = get_sorted_chars(char_counts)

    print("--------- Character Count ------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
main()