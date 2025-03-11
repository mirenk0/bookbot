from stats import num_words, char_count, formatted_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents


def main():
    print("=========== BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    txt_content = get_book_text("./books/frankenstein.txt")
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
