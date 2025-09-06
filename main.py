import sys
from stats import word_count, char_count, sort_char_count

def get_book_text(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()
    
def pretty_print(book_path: str, num_words: int, char_count_list: list):
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ----------")
    for item in char_count_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_txt = get_book_text(book_path)
    num_words = word_count(book_txt)
    char_counts = char_count(book_txt)
    pretty_print(book_path, num_words, sort_char_count(char_counts))

if __name__ == "__main__":
    main()