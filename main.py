def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents


def num_words(txt_content):
    lst_words = txt_content.split()
    return len(lst_words)


def main():
    txt_content = get_book_text("./books/frankenstein.txt")
    print(f"{num_words(txt_content)} words found in the document")


main()
