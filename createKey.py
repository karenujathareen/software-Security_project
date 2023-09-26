import cryptography.fernet as Fernet
import rsa

def KeyGeneration():

    #create private and public key
    (pubkey,privkey) = rsa.newkeys(2048)

    #write a public key
    public_key = open('public_key.key','wb')
    public_key.write(pubkey.save_pkcs1('PEM'))
    public_key.close()

    #write a private key
    private_key = open('private_key.key','wb')
    private_key.write(privkey.save_pkcs1('PEM'))
    private_key.close()


#KeyGeneration()