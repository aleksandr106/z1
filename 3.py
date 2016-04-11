__author__ = 'student'

class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {self.alphabet[i]:self.alphabet[-i-1] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[-i-1].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = dict(lowercase_code)
        self._decode.update(uppercase_code)
    def decode(self,line):
        if len(line)==1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])
    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])


cipher = Atbash()
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()
