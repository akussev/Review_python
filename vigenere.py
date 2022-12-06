from languages import *
import caesar
from cryptographer import Cryptographer
from constants import VERY_BIG_NUMBER, MAX_KEY_SIZE


class Vigenere(Cryptographer):
    def __init__(self, original_string, key, lang):
        self.original_string = original_string
        self.key = key
        self.lang = lang

    def encrypt(self):
        result_string = ''
        cur_index = 0
        for char in self.original_string:
            if char in alphabet[self.lang]:
                result_string += shift[self.lang](char, chars[self.lang][self.key[cur_index % len(self.key)]])
                cur_index += 1
            else:
                result_string += char
        return result_string

    def decrypt(self):
        result_string = ''
        cur_index = 0
        for char in self.original_string:
            if char in alphabet[self.lang]:
                result_string += shift[self.lang](char, -chars[self.lang][self.key[cur_index % len(self.key)]])
                cur_index += 1
            else:
                result_string += char
        return result_string

    def break_in(self):
        alpha_string = ''
        for char in self.original_string:
            if char in alphabet[self.lang]:
                alpha_string += char
        possible_coefficient = VERY_BIG_NUMBER
        right_coefficient = coefficients[self.lang]
        key_size = -1
        for possible_key_size in range(1, min(MAX_KEY_SIZE, len(alpha_string))):
            ans = 0
            for module in range(possible_key_size):
                module_string = alpha_string[module::possible_key_size]
                my_frequency = {char: 0 for char in alphabet[self.lang]}
                for char in module_string:
                    my_frequency[char] += 1
                res = 0
                for value in my_frequency.values():
                    res += (value / len(module_string)) ** 2
                ans += res
            ans /= possible_key_size
            if abs(ans - right_coefficient) < abs(possible_coefficient - right_coefficient):
                possible_coefficient = ans
                key_size = possible_key_size
        key = ""
        for char in range(key_size):
            caesar_breaker = caesar.Caesar(alpha_string[char::key_size], lang=self.lang)
            decryption = caesar_breaker.break_in()
            key += chars[self.lang][(chars[self.lang][alpha_string[char]] - chars[self.lang][decryption[0]]) % len(alphabet[self.lang])]
        print("I think the right key is", key)
        vigenere_decrypter = Vigenere(self.original_string, key, self.lang)
        return vigenere_decrypter.decrypt()
