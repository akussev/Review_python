from languages import *


def encrypt(original_string, delta, lang):
    delta = int(delta)
    result_string = ''
    for char in original_string:
        result_string += shift[lang](char, delta)
    return result_string


def decrypt(original_string, delta, lang):
    delta = int(delta)
    result_string = ''
    for char in original_string:
        result_string += shift[lang](char, -delta)
    return result_string


def break_in(original_string, lang):
    str_map = {char: 0 for char in alphabet[lang]}
    number = 0
    for cur_char in original_string:
        if cur_char in alphabet[lang]:
            str_map[cur_char] += 1
            number += 1
    min_difference = 100000000
    res_shift = -1
    for delta in range(0, len(frequency[lang])):
        diff = 0
        for char in alphabet[lang]:
            diff += abs(str_map[char] / number - frequency[lang][shift[lang](char, -delta)])
        if diff < min_difference:
            min_difference = diff
            res_shift = delta
    return decrypt(original_string, res_shift, lang)
