
def string_to_numbers(text):
    return len(text.split())

def text_to_characters(text):
    char_count = {}
    for characters in text:
        lowercase_char = characters.lower()
        char_count[lowercase_char] = char_count.get(lowercase_char, 0) + 1
    return char_count

def sorted_dictonary(characters):
    result_list = []

    for char, count in characters.items():
        char_info = {'char': char, 'count': count}
        result_list.append(char_info)

    result_list.sort(key=lambda x: x["count"], reverse=True)
    
    return result_list