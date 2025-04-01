def get_num_words(file_as_string):
    """
    This function gets the number of words in a string.
    """
    file_as_list = file_as_string.split()
    return len(file_as_list)

def get_char_num(file_as_string):
    """
    This function gets the number of times a character appears in the string
    """
    char_dict = {}
    for char in file_as_string:
        char_low = char.lower()
        if char_low not in char_dict:
            char_dict[char_low] = 1
        else:
            char_dict[char_low] += 1
    return char_dict

def sort_dict(char_dict):
    """
    This function sorts a dictionary, from highest to lowest count
    """
    def sort_on(dict):
        return dict["count"]

    list_of_dict = []
    for char in char_dict:
        unique_char_dict = {}
        unique_char_dict["character"] = char
        unique_char_dict["count"] = char_dict[char]
        list_of_dict.append(unique_char_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict