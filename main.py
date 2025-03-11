from stats import num_words, char_count, formatted_char_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    txt_content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words(txt_content)} total words")
    word_count = char_count(txt_content)
    print("--------- Character Count -------")
    char_list = formatted_char_count(word_count)
    for i in char_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['count']}")
    print("============= END ===============")


main()
