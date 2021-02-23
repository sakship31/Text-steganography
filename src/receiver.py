from extract import extractFunc
from AES import decrypt
CM_HM=input("Enter cover message:")
password=input("Enter password:")

SM_extract=extractFunc(CM_HM)
print("Your secret message:",decrypt(password,SM_extract))
