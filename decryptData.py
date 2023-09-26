import rsa
def Decryption(role):
    private_key = open('private_key.key','rb')
    prikey = private_key.read()
    prkey = rsa.PrivateKey.load_pkcs1(prikey)

    #read the encrypted file

    if role=='Admin':

       encrypted_data = open("AdminFiles","rb")
       edata = encrypted_data.read()

    elif role=='User':
        encrypted_data = open("UserFiles","rb")
        edata = encrypted_data.read()

    #decrpted the data
    print(rsa.decrypt(edata,prkey).decode())

#Decryption()