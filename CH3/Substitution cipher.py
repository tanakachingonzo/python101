def substitutionEncrypt(plainText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
        for ch in plainText:
            idx = alphabet.find(ch)
            cipherText = cipherText + key[idx]
        return cipherText

# add code here - decrypt()
def decrypt(encrotedText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = ""
        for ch in encrotedText:
            idx = key.find(ch)
            plainText = plainText + alphabet[idx]
        return plainText

key = 'zyxwvutsrqponmlkjihgfedcba '
plainText = 'the quick brown fox'

encriptMssg = substitutionEncrypt(plainText,key)
#print( "Encripted message: " + encriptMssg )

# add code here - invoke decrypt()
#print( "Decripted message: " + decrypt(encriptMssg,key) )

# add code here to:
# 1) ask user for a sentence
# 2) display message
# 3) encrypt message
# 4) decrypt encrypted message

#s = "I like pie"
s = input('Input your message: ')
print( "Original message: " + s )
encriptMssg = substitutionEncrypt(s,key)
print( "Encrypted message: " + encriptMssg )
print( "Decrypted message: " + decrypt(encriptMssg,key) )