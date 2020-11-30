import json
import time
import os
import psutil
from base64 import b64encode, b64decode
from Crypto.Cipher import DES

p = psutil.Process(os.getpid())

key = b'12345678'
cipher = DES.new(key, DES.MODE_CTR, nonce=b'DESCTR')

userIP = open('File 3.docx', 'rb')  # opens a file in read mode
data = userIP.read()  # reads file and replaces new line with space
print("File size is ", os.path.getsize('File 3.docx'), "bytes")

encryptTime = time.time()
ct_bytes = cipher.encrypt(data)
print("Encryption time is ", time.time() - encryptTime, "seconds")
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

encryptFile = open('encryption.txt', 'w')  # creates new file or overwrites existing file
encryptFile.write(ct)  # writes data
encryptFile.close()  # closes the opertaion
print("Encrypted file size is ", os.path.getsize('encryption.txt'), "bytes")
result = json.dumps({'nonce': nonce, 'ciphertext': ct})

try:
    b64 = json.loads(result)
    nonce = b64decode(b64['nonce'])
    ct = b64decode(b64['ciphertext'])
    cipher = DES.new(key, DES.MODE_CTR, nonce=nonce)
    decryptTime = time.time()
    pt = cipher.decrypt(ct)
    print("Decryption time is ", time.time() - decryptTime, "seconds")

    decryptFile = open('decryption.txt', 'wb')
    decryptFile.write(pt)
    decryptFile.close()
    print("Decrypted file size is ", os.path.getsize('decryption.txt'), "bytes")
except (ValueError, KeyError):
    print("Incorrect decryption")
# print("Memory used :", psutil.Process(os.getpid()).memory_info().rss, "bytes")
print("CPU times : ", p.cpu_times())
print("Memory percent used : ", p.memory_percent())
