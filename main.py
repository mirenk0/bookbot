from stats import num_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents


def main():
    txt_content = get_book_text("./books/frankenstein.txt")
    print(f"{num_words(txt_content)} words found in the document")


main()
