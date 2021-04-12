from languages import *
from cryptographer import cryptographer


class caesar(cryptographer):
    def __init__(self, orig_str, key=0, lang='russian'):
        self.original_string = orig_str
        self.key = key
        self.lang = lang

    def encrypt(self):
        key = int(self.key)
        result_string = ''
        for char in self.original_string:
            result_string += shift[self.lang](char, key)
        return result_string

    def decrypt(self):
        key = int(self.key)
        result_string = ''
        for char in self.original_string:
            result_string += shift[self.lang](char, -key)
        return result_string

    def break_in(self):
        str_map = {char: 0 for char in alphabet[self.lang]}
        number = 0
        for cur_char in self.original_string:
            if cur_char in alphabet[self.lang]:
                str_map[cur_char] += 1
                number += 1
        min_difference = 100000000
        res_shift = -1
        for delta in range(0, len(frequency[self.lang])):
            diff = 0
            for char in alphabet[self.lang]:
                diff += abs(str_map[char] / number - frequency[self.lang][shift[self.lang](char, -delta)])
            if diff < min_difference:
                min_difference = diff
                res_shift = delta
        self.key = res_shift
        return self.decrypt()
