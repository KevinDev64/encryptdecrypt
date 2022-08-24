from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from secrets import token_bytes
from typing import Tuple
import os

window = Tk()
window.geometry("600x400") # Screen resolution
key1, key2 = "", ""
encrypt_string = ""

# Functions
def random_key(length: int) -> int:
    # Generate <length> randomized bytes
    tb: bytes = token_bytes(length)
    # Convert this bytes in byte string and return this
    return int.from_bytes(tb, "big")

def exit_func():
    exit()
    
def STRA_error():
    messagebox.showerror('Произошла ошибка! (STR-A)', 'Введена неверная строка!')
    
def DCRS_error():
    messagebox.showerror('Произошла ошибка! (DCR-S)', 'В строке присутствуют недопустимые символы!\nОперация будет прервана!')  
    
def DCR01_error():
    messagebox.showerror('Произошла ошибка! (DCR-01)', 'Ошибка модуля дешифрования!')  
    
def errors():
    os.system("start errors.txt")

def about():
    messagebox.showinfo('О программе', 'EncryptDecrypt v1.0\n\nСделано KevinDev56\n\ne-mail russianbear39157@gmail.com\nTelegram https://t.me/RUSBear08/\nVK https://vk.com/russianbear08/')
    
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

def encrypt_button():
    encr_key1.delete(0, END) # Clear key1 output
    encr_key2.delete(0, END) # Clear key2 output
    
    key1, key2 = "", ""
    
    encrypt_string = encr_in.get()
    if encrypt_string == "":
        STRA_error()
    if encrypt_string != "":
        key1, key2 = encrypt(encrypt_string)

        encr_key1.insert(0, str(key1))
        encr_key2.insert(0, str(key2))

def decrypt_button():
    decrypt_out.delete(0, END)
    key1, key2 = "", ""
    decrypt_string = ""
    
    try:
        key1 = int(decr_key1.get())
        key2 = int(decr_key2.get())
        if key1 == "" or key2 == "":
            STRA_error()
        elif key1 != "" and key2 != "": 
           pass 
    except:
        DCRS_error()
    try:
        result = decrypt(key1, key2)
        
        decrypt_out.insert(0, result)
    except:
        DCR01_error()

tab_control = ttk.Notebook(window) 
 
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Шифратор') 
tab_control.add(tab2, text="Дешифратор")
tab_control.pack(expand=1, fill='both') 

menu = Menu(window, tearoff=0)
file_menu = Menu(menu, tearoff=0)
help_menu = Menu(menu, tearoff=0)

file_menu.add_command(label="Выход", command=exit_func)

help_menu.add_command(label="Справочник ошибок", command=errors)
help_menu.add_command(label="О программе", command=about)

menu.add_cascade(label="Файл", menu=file_menu)
menu.add_cascade(label="Помощь", menu=help_menu)
# Encrypt tab --------------------------------------------------
encr_text = Label(tab1, text="Введите шифруемую строку", font=("Arial", 16))
encr_text.grid(padx=110, pady=0)

encr_in = Entry(tab1, width=30, font=("Arial Bold", 16))
encr_in.focus()
encr_in.grid(padx=110, pady=20)

encr_btn = Button(tab1, text="Зашифровать", command=encrypt_button, font=("Arial", 18))
encr_btn.grid(padx=110, pady=10)

encr_key1_text = Label(tab1, text="Ключ шифратора", font=("Arial Bold", 15))
encr_key1_text.grid(padx=110, pady=10)

encr_key1 = Entry(tab1, width=40, font=("Arial", 13))
encr_key1.grid(padx=20, pady=5)

encr_key2_text = Label(tab1, text="Зашифрованная строка", font=("Arial Bold", 15))
encr_key2_text.grid(padx=110, pady=10)

encr_key2 = Entry(tab1, width=40, font=("Arial", 13))
encr_key2.grid(padx=20, pady=0)

# Decrypt tab ------------------------------------------------
decr_key1_text = Label(tab2, text="Введите ключ шифратора", font=("Arial Bold", 16))
decr_key1_text.grid(padx=110, pady=0)

decr_key1 = Entry(tab2, width=30, font=("Arial", 16))
decr_key1.grid(padx=110, pady=20)
decr_key1.focus()

decr_key2_text = Label(tab2, text="Введите зашифрованную строку", font=("Arial Bold", 16))
decr_key2_text.grid(padx=110, pady=0)

decr_key2 = Entry(tab2, width=30, font=("Arial", 16))
decr_key2.grid(padx=110, pady=10)

decrypt_btn = Button(tab2, text="Расшифровать", font=("Arial", 18), command=decrypt_button)
decrypt_btn.grid(padx=110, pady=10)

decrypt_out_text = Label(tab2, text="Расшифрованная строка", font=("Arial Bold", 15))
decrypt_out_text.grid(padx=110, pady=20)

decrypt_out = Entry(tab2, width=40, font=("Arial", 13))
decrypt_out.grid(padx=110, pady=10)

window.title("EncryptDecrypt V1.0")
window.iconbitmap("EncryptDecrypt.ico")
window.config(menu=menu)
window.minsize(600, 400)
window.maxsize(600, 400)
window.mainloop()