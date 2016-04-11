__author__ = 'student'
import random
class Monoalphabet:
    alphabet ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
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

line=input()
a=[[0]*2 for i in range(33)]
l=''+line
l=l.lower()
alphabet=set()
k=0
for i in Monoalphabet.alphabet:
    alphabet.add(i)
    a[k][0]=i
    k+=1
print(a)
k=0
for i in l:
    if i in alphabet:
        a[i][1]+=1
    print(a)
for i in range(33):
    for j in range(i,33):
        if a[i][1]>a[j][0]:
            a[i],a[j]=a[j],a[i]
print(a)

'''' key = Monoalphabet.alphabet[:]
    l=list(key)
    random.shuffle(l)
    key=''.join(l)
    cipher = Monoalphabet(key)
    print(cipher.encode(line))'''