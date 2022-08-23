from secrets import token_bytes
from typing import Tuple
import os
import time

def random_key(length: int) -> int:
    # Generate <length> randomized bytes
    tb: bytes = token_bytes(length)
    # Convert this bytes in byte string and return this
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR Function
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR Function
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    # key1, key2 = encrypt(input("Enter a string >> "))
    # print("KEY 1 >> " + str(key1)+ "\n\nKEY 2 >> " + str(key2) + "\n\n")
    # result: str = decrypt(key1, key2)
    # print(result)
    f = None 
    
    while True:
        os.system('cls')
        f = input("""Select function:
              1) Encrypt
              2) Decrypt
              3) About
              4) Exit
              
              >> """)
        
        if f == "1" or f == "Encrypt" or f == "encrypt":
            os.system('cls')
            key1, key2 = "", ""
            
            res = input("Enter a string for encrypter >> ")
            
            if res == "":
                os.system('cls')
                print("Invalid string!  --> (STR-A) \nExiting!")
                exit()
                
            elif res != "1":
                os.system('cls')
                print("Encrypting...")
                key1, key2 = encrypt(res)
                print("Done! Encrypted string:") 
                print("KEY >> " + str(key1))
                print("\nEncrypted string >> " + str(key2))
                input("\nCopy & Save this! After, press Enter >> ")
                os.system('cls')
                
        if f == "Decrypt" or f == "decrypt" or f == "2":
            os.system('cls')
            key1, key2 = "", ""
            
            
            try:
                key1 = int(input("Enter the key for decrypter >> "))    
                key2 = int(input("Enter the encrypted string >> ")) # Try & except
                if key1 == "":
                    os.system('cls')
                    print("Invalid string!  --> (STR-A) \nExiting!")
                    exit()
                if key2 == "":
                    os.ystem('cls')
                    print("Invalid string!  --> (STR-A) \nExiting!")
                    exit()
                os.system('cls')
                print("Decrypting...")
            except:
                os.system('cls')
                print("FATAL error ocurred! --> (DCR-S) \nPlease check the decryptor key and encrypted string for characters other than numbers!\nReturing to main menu!")
                input("\nPress Enter to continue!")
                
            
            try:
                result = decrypt(key1, key2)
                print("Decrypted! ")
                print("\nResult >> " + result)
                input("\nCopy & Save this result! After, press Enter >> ")
                
            except:
                os.system('cls')
                print("Error ocurred!  --> (DCR-01) \nCheck the key and encrypted string! \nReturing to main menu!")
                input("\nPress Enter to continue >> ")
            os.system('cls')
            
        if f == "About" or f == "about" or f == "3":
            os.system('cls')
            print("EncryptDecrypt v.0.1\n\nMade by KevinDev56")
            input("\n\nPress Enter >> ")
            os.system('cls')
            
        if f == "Exit" or f == "exit" or f == "4":
            break
    
