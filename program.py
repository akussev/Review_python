import caesar
import vigenere
import languages
import steganography
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['caesar', 'vigenere', 'steganography'], type=str)

    return parser


def which_lang(string):
    rus = False
    eng = False
    for i in string:
        if i in languages.alphabet['russian']:
            rus = True
        if i in languages.alphabet['english']:
            eng = True
    if rus and eng:
        raise UnicodeError("I can't understand what language you use here.")
    return 'russian' if rus else 'english'


class Program:
    modes = {'caesar': caesar.caesar, 'vigenere': vigenere.vigenere, 'steganography': steganography.steganography}

    def do_crypt(self):
        parser = argparse.ArgumentParser(prog='Cryptographer')
        subparsers = parser.add_subparsers(help="Mode commands")

        parser_caesar = subparsers.add_parser('caesar', help="Actions for caesar")
        parser_caesar.add_argument('-a', '--action', choices=['encrypt', 'decrypt', 'break_in'], help="Action name")
        parser_caesar.add_argument('-f', '--file', help="Way to file")
        subparsers_caesar = parser_caesar.add_subparsers()
        parser_caesar.add_argument('-k', '--key', type=int, default=0, help="Shift for caesar (not specified if action == break_in)")
        parser_caesar.add_argument('--mode', default='caesar')

        parser_vigenere = subparsers.add_parser('vigenere', help="Actions for vigenere")
        parser_vigenere.add_argument('-a', '--action', choices=['encrypt', 'decrypt', 'break_in'], help="Action name")
        parser_vigenere.add_argument('-f', '--file', help="Way to file")
        parser_vigenere.add_argument('-k', '--key', default="", help="Key for vigenere (not specified if action == break_in)")
        parser_vigenere.add_argument('--mode', default='vigenere')

        parser_steganography = subparsers.add_parser('steganography', help="Actions for steganography")
        parser_steganography.add_argument('-a', '--action', choices=['encrypt', 'decrypt'], help="Action name")
        parser_steganography.add_argument('-f', '--way_to_bmp', help="Way to picture")
        parser_steganography.add_argument('-k', '--key', help="Key to steganography")
        parser_steganography.add_argument('-s', '--secret_message', default="", help="Message to hide (not specified if action == decrypt")
        parser_steganography.add_argument('--mode', default='steganography')

        args = parser.parse_args()
        mode = args.mode
        action = args.action
        if mode == 'caesar' or mode == 'vigenere':
            file = args.file
            key = args.key
            with open(file, 'r') as input_file:
                original_string = input_file.read()
            original_string = original_string.lower()
            lang = which_lang(original_string)
            result = ''
            program = self.modes[mode](original_string, key, lang)
            if action == 'break_in':
                result = program.break_in()
            elif action == 'decrypt':
                result = program.decrypt()
            elif action == 'encrypt':
                result = program.encrypt()
            with open("answer.txt", "w+") as output_file:
                output_file.write(result)
        elif mode == 'steganography':
            way_to_bmp = args.way_to_bmp
            key = args.key
            program = steganography.steganography(way_to_bmp, key)
            if action == 'encrypt':
                way_to_secret_message = args.secret_message
                with open(way_to_secret_message, 'r') as input_file:
                    program.original_string = input_file.read()
                program.encrypt()
            elif action == 'decrypt':
                result = program.decrypt()
                with open("answer.txt", "w+") as output_file:
                    output_file.write(result)
