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


def formatted_char_count(count_dict):
    dict_list = []

    for k, c in count_dict.items():
        dict_list.append({"char": k, "count": c})

    dict_list.sort(key=lambda d: d["count"], reverse=True)

    return dict_list
