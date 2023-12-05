def read_input(text):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

def decode_integers():
    sum_of_digits = 0
    for i in read_input('text'):
        chars = list(i)
        first_digit = next((x for x in chars if x.isdigit()), None)
        second_digit = next((x for x in chars[::-1] if x.isdigit()), None)

        final_digit = int(first_digit + second_digit)
        sum_of_digits += final_digit
    return sum_of_digits

num_dictionary = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        }

def replace_number_with_word(string):
    for word, number in num_dictionary.items():
        string = string.replace(str(number), word)
    return string

def find_substrings_with_digits(string):
    substring_with_indices = []

    for word in num_dictionary.keys():
        index = string.find(word)
        while index != -1:
            substring_with_indices.append((word, index))
            index = string.find(word, index + 1)

    substring_with_indices.sort(key=lambda x: x[1])

    substrings_translated = [num_dictionary[word] for word, _ in substring_with_indices]
    return substrings_translated

def decode_integers_from_words():
    second_sum_of_digits = 0

    for i in read_input('text'):
        string = replace_number_with_word(i)
        substring = find_substrings_with_digits(string)

        first_digit = substring[0]
        last_digit = substring[-1]
        final_digit = first_digit*10 + last_digit

        second_sum_of_digits += final_digit

    return second_sum_of_digits

if __name__ == "__main__":
    print("Answer to 1: {}".format(decode_integers()))
    print("Answer to 2: {}".format(decode_integers_from_words()))
