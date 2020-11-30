import timeit
import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import DES


import os, psutil
p = psutil.Process(os.getpid())


####################_encryption_###################



def enc_time():

    file_data=open("File 3.docx",'rb')
    data=file_data.read()
    file_data.close()
    global key
    key =b'somaiyaa'
    cipher = DES.new(key, DES.MODE_OFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    global ct
    ct = b64encode(ct_bytes).decode('utf-8')
    global result
    result=ct
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    file_enc=open("encrypt.txt",'w')
    file_enc.write(ct)
    file_enc.close()

enc_time()

print("Encryption_time:",timeit.timeit(enc_time,number=1))
print("cpu times:",p.cpu_times())
print ("memory usage percent:",p.memory_percent())


##################_decryption_code_#################

def dec_time():

    ciphertext=ct
    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct1 = b64decode(b64['ciphertext'])
        cipher = DES.new(key, DES.MODE_OFB, iv=iv)
        pt = cipher.decrypt(ct1)

        file_dec=open("decrypt.txt",'wb')
        file_dec.write(pt)
        file_dec.close()

    except (ValueError, KeyError):
        print("Incorrect decryption")
dec_time()

print("Decryption_time:",timeit.timeit(dec_time,number=1))
print("cpu times:",p.cpu_times())
print ("memory usage percent:",p.memory_percent())

