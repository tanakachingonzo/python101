def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

# add code here - decrypt() function - pb. 4)b)

def decrypt(encryptedText, key):
    decryptkey = 'abcdefghijklmnopqrstuvwxyz '
    plainText = ""
    for ch in encryptedText:
        idx=key.find(ch)
        plainText=plainText+decryptkey[idx]
    return plainText

key = 'zyxwvutsrqponmlkjihgfedcba '
plainText = 'the quick brown fox'

encryptMssg = substitutionEncrypt(plainText, key)
# print("Encripted message: " + encryptMssg)

# add code here to invoke decrypt() - pb. 4)c)

encryptMssg = substitutionEncrypt(plainText, key)
#print("Decrypted message: " + decrypt(encryptMssg,key)



# pb. 4)d)
# add code here to:
#    1) ask user for a sentence
#    2) display message
#    3) encrypt message
#    4) decrypt encrypted message

s = input("Input message for a sentence:")
print ("Original message:", decryptMssg + s)
print("Encrypted message: "+encryptMssg)
decrypt(s, key)