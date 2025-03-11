def num_words(txt_content):
    lst_words = txt_content.split()
    return len(lst_words)


def char_count(txt_content):
    count_dict = {}
    for c in txt_content:
        c_lowered = c.lower()
        if c_lowered in count_dict:
            count_dict[c_lowered] += 1
        else:
            count_dict[c_lowered] = 1

    return count_dict
