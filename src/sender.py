import sys
sys.path

from embed import embedFunc
from extract import extractFunc
from AES import encrypt,decrypt
import pyperclip as py

# SM=input("Enter secret message:")
# CM=input("Enter cover message:")
# password=input("Enter password for encryption:")

def hideFunc(SM,password,CM):
    encSM=encrypt(password,SM)
    print("Encrypted secret message going to send:",encSM)
    CM_HM=embedFunc(encSM,CM)
    print("Cover message=",CM_HM)
    py.copy(CM_HM)
    return CM_HM
    

#print("copy this message and paste it to send")


