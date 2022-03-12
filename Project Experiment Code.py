import onetimepad
import random
import string
import datetime
import hashlib
from cryptography.fernet import Fernet
message_input=str(input())
temp1=message_input[::-1]
key=Fernet.generate_key()
fernet=Fernet(key)
encMessage=fernet.encrypt(message_input.encode())
final_Data=str(encMessage)      
print(final_Data)                   
