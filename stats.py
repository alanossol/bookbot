
def get_num_words(text):
    words = text.split()
    number_words = len(words)
    return number_words


def get_count_chars(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on_num(list):
    return list["num"]

def get_sort_chars_list(dictionary):
    my_list = []
    for char, count in dictionary.items():
        my_list.append({"char": char, "num": count})
    
    
    my_list.sort(reverse=True, key=sort_on_num)
    return my_list
