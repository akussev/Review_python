from PIL import Image, ImageDraw
from cryptographer import cryptographer


def string_hash(key):
    p = 31
    power = 1
    ans = 0
    for i in range(len(key)):
        ans += ord(key[i]) * power
        power *= p
        power %= 2 ** 64
        ans %= 2 ** 64
    return ans


def pixel_generator(key_hash):
    cur = key_hash
    while True:
        cur = (6364136223846793005 * cur + 271828182890459) % (2 ** 64)
        yield cur


class steganography(cryptographer):
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
            x = (pixel % (2 ** 32)) % width
            y = ((pixel >> 32) % (2 ** 32)) % height
            if used[x][y]:
                continue
            used[x][y] = True
            res_ord = ord(self.original_string[cur_char])
            res_ord = res_ord if res_ord < 600 else res_ord - 600
            first = res_ord >> 6 % 8
            second = (res_ord >> 3) % 8
            third = res_ord % 8
            red = ((pix[x, y][0] >> 3) << 3) | first
            green = ((pix[x, y][1] >> 3) << 3) | second
            blue = ((pix[x, y][2] >> 3) << 3) | third
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
            x = (pixel % (2 ** 32)) % width
            y = ((pixel >> 32) % (2 ** 32)) % height
            if used[x][y]:
                continue
            used[x][y] = True
            first = pix[x, y][0] % 8
            second = pix[x, y][1] % 8
            third = pix[x, y][2] % 8
            res_ord = (first << 6) | (second << 3) | third
            char = chr(res_ord if res_ord < 400 else res_ord + 600)
            if char == '\0':
                break
            result += char
        return result
