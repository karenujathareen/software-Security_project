from cryptography.fernet import Fernet
import rsa
import base64

def Encryption(message,role):
    public_key = open('public_key.key','rb')
    pubkey = public_key.read()

    message = message.encode("utf-8")
    #message_base = message[:32].ljust(32,b'\x00')
    #message_base64 = base64.urlsafe_b64encode(message_base)

    #encrypt the data
    pubkey = rsa.PublicKey.load_pkcs1(pubkey)
    encrypted_data = rsa.encrypt(message,pubkey)

    #write encrypted_data

    if role=='Admin':

        edata = open ("AdminFiles","wb")
        edata.write(encrypted_data)
    elif role=='User':
        edata = open ("UserFiles","wb")
        edata.write(encrypted_data)

#Encryption("Hello"