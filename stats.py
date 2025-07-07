# This creates a funtion "count_words" and takes one parameter "text" in, which should be a string.
def get_num_words(text):
    words = text.split()    #.split devides the string into a list of words by splitting it at whitespaces
    return len(words)       # returns the number of words by counting the length of the list

def get_char_count(text):
    char_counts = {}
    for char in text.lower(): #convert to lowercase to merge cases
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_chars(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # skip non-alphbetical chars
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list