def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_dict = {}
    for c in text:
        lower_char = c.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict


def sorted_dict(char_dict):
    sorted_list = []
    for c in char_dict:
        sorted_list.append({"char": c, "num": char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(items):
    return items["num"]
