def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    count = get_word_cout(text)
    char_count = charater_count(text)
    char_sorted_list = chars_dict_to_sorted_dict(char_count)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_cout(text):
    words = text.split()
    return len(words)

def charater_count(text):
    lowered_text = text.lower()
    char_dict = {}
    for n in lowered_text:
        if n not in char_dict:
            char_dict[n] = 1
        char_dict[n] += 1
    return char_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_dict(nums_char_dict):
    sorted_list = []
    for ch in nums_char_dict:
        sorted_list.append({"char": ch, "num": nums_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
main()