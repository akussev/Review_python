russian = {
    'а': 0.0801,
    'б': 0.0159,
    'в': 0.0454,
    'г': 0.0170,
    'д': 0.0298,
    'е': 0.0845,
    'ё': 0.0004,
    'ж': 0.0094,
    'з': 0.0165,
    'и': 0.0735,
    'й': 0.0121,
    'к': 0.0349,
    'л': 0.0440,
    'м': 0.0321,
    'н': 0.0670,
    'о': 0.1097,
    'п': 0.0281,
    'р': 0.0473,
    'с': 0.0547,
    'т': 0.0626,
    'у': 0.0262,
    'ф': 0.0026,
    'х': 0.0097,
    'ц': 0.0048,
    'ч': 0.0144,
    'ш': 0.0073,
    'щ': 0.0036,
    'ъ': 0.0004,
    'ы': 0.0190,
    'ь': 0.0174,
    'э': 0.0032,
    'ю': 0.0064,
    'я': 0.0201
}

russian_num = {
    'а': 0,
    'б': 1,
    'в': 2,
    'г': 3,
    'д': 4,
    'е': 5,
    'ё': 6,
    'ж': 7,
    'з': 8,
    'и': 9,
    'й': 10,
    'к': 11,
    'л': 12,
    'м': 13,
    'н': 14,
    'о': 15,
    'п': 16,
    'р': 17,
    'с': 18,
    'т': 19,
    'у': 20,
    'ф': 21,
    'х': 22,
    'ц': 23,
    'ч': 24,
    'ш': 25,
    'щ': 26,
    'ъ': 27,
    'ы': 28,
    'ь': 29,
    'э': 30,
    'ю': 31,
    'я': 32
}

new_dict = russian_num.copy()
for pair in new_dict.items():
    russian_num[pair[1]] = pair[0]

english = {
    'a': 0.0820,
    'b': 0.0150,
    'c': 0.0280,
    'd': 0.0430,
    'e': 0.1300,
    'f': 0.0220,
    'g': 0.0200,
    'h': 0.0610,
    'i': 0.0700,
    'j': 0.0015,
    'k': 0.0077,
    'l': 0.0400,
    'm': 0.0240,
    'n': 0.0670,
    'o': 0.0750,
    'p': 0.0190,
    'q': 0.00095,
    'r': 0.0600,
    's': 0.0630,
    't': 0.0910,
    'u': 0.0280,
    'v': 0.0098,
    'w': 0.0240,
    'x': 0.0015,
    'y': 0.0200,
    'z': 0.00074
}

english_num = {i: chr(i + 97) for i in range(26)}
for j in range(26):
    english_num[chr(j + 97)] = j


def russian_shift(char, delta):
    return russian_num[(russian_num[char] + delta) % 33] if char in russian.keys() else char


def english_shift(char, delta):
    return english_num[(english_num[char] + delta) % 26] if char in english.keys() else char


shift = {
    'russian': russian_shift,
    'english': english_shift
}

frequency = {
    'russian': russian,
    'english': english
}

chars = {
    'russian': russian_num,
    'english': english_num
}

coefficients = {
    'russian': 0.0553,
    'english': 0.0644
}

alphabet = {
    'russian': ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'],
    'english': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

}
