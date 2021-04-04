languages = dict()

russian = dict()
russian_num = dict()
russian['а'] = 0.0801
russian['б'] = 0.0159
russian['в'] = 0.0454
russian['г'] = 0.0170
russian['д'] = 0.0298
russian['е'] = 0.0845
russian['ё'] = 0.0004
russian['ж'] = 0.0094
russian['з'] = 0.0165
russian['и'] = 0.0735
russian['й'] = 0.0121
russian['к'] = 0.0349
russian['л'] = 0.0440
russian['м'] = 0.0321
russian['н'] = 0.0670
russian['о'] = 0.1097
russian['п'] = 0.0281
russian['р'] = 0.0473
russian['с'] = 0.0547
russian['т'] = 0.0626
russian['у'] = 0.0262
russian['ф'] = 0.0026
russian['х'] = 0.0097
russian['ц'] = 0.0048
russian['ч'] = 0.0144
russian['ш'] = 0.0073
russian['щ'] = 0.0036
russian['ъ'] = 0.0004
russian['ы'] = 0.0190
russian['ь'] = 0.0174
russian['э'] = 0.0032
russian['ю'] = 0.0064
russian['я'] = 0.0201
russian_num['а'] = 0
russian_num['б'] = 1
russian_num['в'] = 2
russian_num['г'] = 3
russian_num['д'] = 4
russian_num['е'] = 5
russian_num['ё'] = 6
russian_num['ж'] = 7
russian_num['з'] = 8
russian_num['и'] = 9
russian_num['й'] = 10
russian_num['к'] = 11
russian_num['л'] = 12
russian_num['м'] = 13
russian_num['н'] = 14
russian_num['о'] = 15
russian_num['п'] = 16
russian_num['р'] = 17
russian_num['с'] = 18
russian_num['т'] = 19
russian_num['у'] = 20
russian_num['ф'] = 21
russian_num['х'] = 22
russian_num['ц'] = 23
russian_num['ч'] = 24
russian_num['ш'] = 25
russian_num['щ'] = 26
russian_num['ъ'] = 27
russian_num['ы'] = 28
russian_num['ь'] = 29
russian_num['э'] = 30
russian_num['ю'] = 31
russian_num['я'] = 32
new_dict = russian_num.copy()
for pair in new_dict.items():
    russian_num[pair[1]] = pair[0]


english = dict()
english_num = dict()
english['a'] = 0.0820
english['b'] = 0.0150
english['c'] = 0.0280
english['d'] = 0.0430
english['e'] = 0.1300
english['f'] = 0.0220
english['g'] = 0.0200
english['h'] = 0.0610
english['i'] = 0.0700
english['j'] = 0.0015
english['k'] = 0.0077
english['l'] = 0.0400
english['m'] = 0.0240
english['n'] = 0.0670
english['o'] = 0.0750
english['p'] = 0.0190
english['q'] = 0.00095
english['r'] = 0.0600
english['s'] = 0.0630
english['t'] = 0.0910
english['u'] = 0.0280
english['v'] = 0.0098
english['w'] = 0.0240
english['x'] = 0.0015
english['y'] = 0.0200
english['z'] = 0.00074
for i in range(26):
    english_num[i] = chr(i + 97)
    english_num[chr(i + 97)] = i


def russian_shift(char, delta):
    return russian_num[(russian_num[char] + delta) % 33] if char in russian.keys() else char


def english_shift(char, delta):
    return english_num[(english_num[char] + delta) % 26] if char in english.keys() else char


shift = dict()
shift['russian'] = russian_shift
shift['english'] = english_shift

frequency = dict()
frequency['russian'] = russian
frequency['english'] = english

chars = dict()
chars['russian'] = russian_num
chars['english'] = english_num

coefficients = dict()
coefficients['russian'] = 0.0553
coefficients['english'] = 0.0644

alphabet = dict()
alphabet['russian'] = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet['english'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
