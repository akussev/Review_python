import caesar
import vigenere
import languages
import steganography


class Program:
    actions = dict()
    modes = []

    def __init__(self):
        self.actions[('caesar', 'encrypt')] = caesar.encrypt
        self.actions[('caesar', 'decrypt')] = caesar.decrypt
        self.actions[('caesar', 'break_in')] = caesar.break_in
        self.actions[('vigenere', 'encrypt')] = vigenere.encrypt
        self.actions[('vigenere', 'decrypt')] = vigenere.decrypt
        self.actions[('vigenere', 'break_in')] = vigenere.break_in
        self.actions[('steganography', 'encrypt')] = steganography.encrypt
        self.actions[('steganography', 'decrypt')] = steganography.decrypt
        self.modes = ['caesar', 'vigenere', 'steganography']

    def which_lang(self, string):
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


    def do_crypt(self, args):
        if len(args) < 3:
            raise NameError("Too few arguments")
        mode = args[0]
        action = args[1]
        file = args[2]
        if mode not in self.modes:
            raise NameError("Wrong mode name")
        if (mode, action) not in self.actions.keys():
            raise NameError("Wrong action name")
        if mode == 'caesar' or mode == 'vigenere':
            with open(file, 'r') as input_file:
                original_string = input_file.read()
            original_string = original_string.lower()
            lang = self.which_lang(original_string)
            result = ''
            if action == 'break_in' and len(args) == 3:
                result = self.actions[(mode, action)](original_string, lang)
            elif action == 'encrypt' or action == 'decrypt' and len(args) == 4:
                key = args[3]
                result = self.actions[(mode, action)](original_string, key, lang)
            else:
                raise NameError("Wrong arguments for this mode")
            with open("answer.txt", "w+") as output_file:
                output_file.write(result)
        elif mode == 'steganography':
            if action == 'encrypt' and len(args) == 5:
                with open(file, 'r') as input_file:
                    original_string = input_file.read()
                key = args[3]
                picture = args[4]
                steganography.encrypt(original_string, key, picture)
            elif action == 'decrypt' and len(args) == 4:
                key = args[3]
                result = steganography.decrypt(file, key)
                with open("answer.txt", "w+") as output_file:
                    output_file.write(result)
