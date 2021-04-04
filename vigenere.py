from languages import *
import caesar


def encrypt(original_string, key, lang):
    result_string = ''
    cur_index = 0
    for char in original_string:
        if char in alphabet[lang]:
            result_string += shift[lang](char, chars[lang][key[cur_index % len(key)]])
            cur_index += 1
        else:
            result_string += char
    return result_string


def decrypt(original_string, key, lang):
    result_string = ''
    cur_index = 0
    for char in original_string:
        if char in alphabet[lang]:
            result_string += shift[lang](char, -chars[lang][key[cur_index % len(key)]])
            cur_index += 1
        else:
            result_string += char
    return result_string


def break_in(original_string, lang):
    alpha_string = ''
    for char in original_string:
        if char in alphabet[lang]:
            alpha_string += char
    possible_coefficient = 10000
    right_coefficient = coefficients[lang]
    key_size = -1
    for possible_key_size in range(1, 100):
        ans = 0
        for module in range(possible_key_size):
            module_string = alpha_string[module::possible_key_size]
            my_frequency = {char: 0 for char in alphabet[lang]}
            for char in module_string:
                my_frequency[char] += 1
            res = 0
            for value in my_frequency.values():
                res += (value / len(module_string)) ** 2
            ans += res
        ans /= possible_key_size
        print(possible_key_size, ans)
        if abs(ans - right_coefficient) < abs(possible_coefficient - right_coefficient):
            possible_coefficient = ans
            key_size = possible_key_size
    key = ""
    for char in range(key_size):
        decryption = caesar.break_in(alpha_string[char::key_size], lang)
        key += chars[lang][(chars[lang][alpha_string[char]] - chars[lang][decryption[0]]) % len(alphabet[lang])]
    print(key, key_size)
    return decrypt(original_string, key, lang)
