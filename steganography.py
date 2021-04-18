from PIL import Image, ImageDraw
from cryptographer import Cryptographer
from constants import *


def string_hash(key):
    p = PRIME_HASH
    power = 1
    ans = 0
    for i in range(len(key)):
        ans += ord(key[i]) * power
        power *= p
        power %= MODULE
        ans %= MODULE
    return ans


def pixel_generator(key_hash):
    cur = key_hash
    while True:
        cur = (MULTIPLIER * cur + INCREMENT) % MODULE
        yield cur


class Steganography(Cryptographer):
    original_string = ""
    way_to_bmp = ""

    def __init__(self, way_to_bmp, key):
        self.key = key
        self.way_to_bmp = way_to_bmp

    def encrypt(self):
        image = Image.open(self.way_to_bmp)
        width = image.size[0]
        height = image.size[1]
        draw = ImageDraw.Draw(image)
        pix = image.load()
        self.original_string += '\0'
        if height * width < len(self.original_string):
            return
        used = [[False for y in range(height)] for x in range(width)]
        cur_char = 0
        for pixel in pixel_generator(string_hash(self.key)):
            x = (pixel % HALF_MODULE) % width
            y = ((pixel >> LOG_OF_HALF_MODULE) % HALF_MODULE) % height
            if used[x][y]:
                continue
            used[x][y] = True
            res_ord = ord(self.original_string[cur_char])
            res_ord = res_ord if res_ord < 600 else res_ord - 600
            first = res_ord >> (2 * THIRD_OF_BIT_MASK) % (1 << THIRD_OF_BIT_MASK)
            second = (res_ord >> THIRD_OF_BIT_MASK) % (1 << THIRD_OF_BIT_MASK)
            third = res_ord % 8
            red = ((pix[x, y][0] >> THIRD_OF_BIT_MASK) << THIRD_OF_BIT_MASK) | first
            green = ((pix[x, y][1] >> THIRD_OF_BIT_MASK) << THIRD_OF_BIT_MASK) | second
            blue = ((pix[x, y][2] >> THIRD_OF_BIT_MASK) << THIRD_OF_BIT_MASK) | third
            draw.point((x, y), (red, green, blue))
            if self.original_string[cur_char] == '\0':
                break
            cur_char += 1
        image.save('result.bmp')

    def decrypt(self):
        result = ''
        image = Image.open(self.way_to_bmp)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()
        used = [[False for y in range(height)] for x in range(width)]
        for pixel in pixel_generator(string_hash(self.key)):
            x = (pixel % HALF_MODULE) % width
            y = ((pixel >> LOG_OF_HALF_MODULE) % HALF_MODULE) % height
            if used[x][y]:
                continue
            used[x][y] = True
            first = pix[x, y][0] % (1 << THIRD_OF_BIT_MASK)
            second = pix[x, y][1] % (1 << THIRD_OF_BIT_MASK)
            third = pix[x, y][2] % (1 << THIRD_OF_BIT_MASK)
            res_ord = (first << (2 * THIRD_OF_BIT_MASK)) | (second << THIRD_OF_BIT_MASK) | third
            char = chr(res_ord if res_ord < 400 else res_ord + 600)
            if char == '\0':
                break
            result += char
        return result
