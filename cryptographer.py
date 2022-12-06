from abc import abstractmethod

class Cryptographer:
    original_string = ""
    key = ""
    lang = None

    @abstractmethod
    def encrypt(self):
        raise Exception("I don't know what to encrypt")

    @abstractmethod
    def decrypt(self):
        raise Exception("I don't know what to decrypt")

    @abstractmethod
    def break_in(self):
        raise Exception("I don't know what to break-in")
