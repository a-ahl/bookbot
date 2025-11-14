def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_character_frequency(text):
    """takes a string, returns a dict of characer: frequency"""
    char_frequency = {}
    lower_text = text.lower()
    characters = list(lower_text)
    for char in characters:
        if char in char_frequency:
            char_frequency[char]+=1
        else:
            char_frequency[char] = 1

    return char_frequency

def get_num(dict):
    return dict["num"]

def get_sorted_dict_list(dict):
    dict_list = []
    for key, value in dict.items():
        pair_dict = {}
        pair_dict["char"] = key
        pair_dict["num"] = value
        dict_list.append(pair_dict)
    
    # sort list desc
    dict_list.sort(key=get_num, reverse=True)

    return dict_list