__author__ = 'student'


class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        l={self.alphabet[i]:self.alphabet[(i-key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        u={self.alphabet[i].upper():self.alphabet[(i-key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(l)
        self._encode.update(u)
        self._decode = dict(lowercase_code)
        self._decode.update(uppercase_code)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])

key = 17
cipher = Caesar(key)
line = input()
while line:
    print(cipher.decode(line))
    line=input()
    '''print(cipher.encode(line))'''
