import docx
from Crypto.Cipher import DES
import time
#pip install python-docx
#pip install pycryptodomex --no-binary :all:

def ecb_encrypt(key, plain):
    cipher = DES.new(key, DES.MODE_ECB)
    msg = cipher.encrypt(plain)
    newOne(msg, "encrypt.txt")
    return msg

def ecb_decrypt(key, ct):
    cipher = DES.new(key, DES.MODE_ECB)
    mes = cipher.decrypt(ct)
    newOne(mes, "decrypt.txt")
    return mes


def gettext(filename):
    ans = b""
    with open(filename, 'rb') as fileInput:
        for line in fileInput: ans += line
    return ans

def check_len(textlen):
    if textlen % 8 == 0:
        return 0
    else:
        return textlen % 8

def writedown(filename, text):
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(filename)


def newOne(text, path):
    f = open(path, "wb")
    f.write(text)
    f.close()

def balance(b, a):
    if b<4:
        for i in range(8-b):
            a=a+b' '
    else:
        a = a+b' '
    return a

start = time.time()
a = gettext('File_1.docx')
# a = docc
ans = check_len(len(a))
a = balance(ans,a)
cc = ecb_encrypt(b'srinathn', a)

print(ecb_decrypt(b'srinathn',cc))
# ecb_decrypt('srinathn', cc)
print(time.time()-start)


