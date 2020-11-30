#!/usr/bin/python3 
import os, psutil
p = psutil.Process(os.getpid())
from Crypto import Random 
from Crypto.Cipher import AES 
import os 
import os.path 
from os import listdir 
from os.path import isfile, join 
import time 
class Encryptor:
    def __init__(self, key): 
        self.key = key 


    def pad(self, s): 
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size) 


    def encrypt(self, message, key, key_size=128): 
        tic = time.time()
        message = self.pad(message) 
        iv = Random.new().read(AES.block_size) 
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ans =  iv + cipher.encrypt(message)
        toc = time.time() 
        print(f"Enc Time: {toc-tic}")
        time.sleep(5)
        return ans


    def encrypt_file(self, file_name): 
        with open(file_name, 'rb') as fo: 
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key) 
        with open(file_name + ".enc", 'wb') as fo: 
            fo.write(enc) 
            os.remove(file_name) 


    def decrypt(self, ciphertext, key): 
        tic = time.time()
        iv = ciphertext[:AES.block_size] 
        cipher = AES.new(key, AES.MODE_CBC, iv) 
        plaintext = cipher.decrypt(ciphertext[AES.block_size:]) 
        toc = time.time()
        print(f"DEcrryption Time: {toc-tic}")
        time.sleep(5)
        return plaintext.rstrip(b"\0") 


    def decrypt_file(self, file_name): 
        with open(file_name, 'rb') as fo: 
            ciphertext = fo.read() 
        dec = self.decrypt(ciphertext, self.key) 
        with open(file_name[:-4], 'wb') as fo: 
            fo.write(dec)
        os.remove(file_name) 


key =b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key) 
clear = lambda: os.system('clear') 
if os.path.isfile('data.txt.enc'): 
    while True: 
         password = str(input("Password: ")) 
         enc.decrypt_file("data.txt.enc") 
         p = '' 
         with open("data.txt", "r") as f: 
             p = f.readlines() 
         if p[0] == password: 
             enc.encrypt_file("data.txt") 
             break
    while True:
        choice = int(input("1. Encode \n 2. Decode"))
        if choice == 1: 
            enc.encrypt_file(str(input("File name: ")))
        elif choice == 2: 
            enc.decrypt_file(str(input("File name: ")))

else: 
    while True: 
        clear() 
        password = str(input("Enter password: ")) 
        repassword = str(input("Confirm password: ")) 
        if password == repassword: 
            break 
        else: 
            print("Passwords Incorrect!")
    f = open("data.txt","w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")

