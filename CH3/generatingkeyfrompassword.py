def removeDupes(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr


def removeMatches(myString, removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr


def genKeyFromPass(password):
    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx + 1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

    # add your code here

password = input("Password: ")
key = genKeyFromPass(password)
print("Key:",key)
plainText= input("Enter message to be encrypted: ")

def substitutionEncrypt(plainText, key):
    plainText=plainText.lower()
    cipherText=""
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for ch in plainText:
        idx=alphabet.find(ch)
        cipherText= cipherText +key[idx]
    return cipherText

def decrypt(encryptedText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    for ch in encryptedText:
        idx= key.find(ch)
        plainText= plainText+alphabet[idx]
    return plainText

pswd=input("Input pswd: ")
key= genKeyFromPass(pswd)
print( "Your encryption key is: " +key)

txt= input("Input text you would like to encrypt: ")
txtEncrypted= substitutionEncrypt(txt, key+' ')
print("Your text encrypted is: " +txtEncrypted )
print("Your text decrypted is: "+ decrypt(txtEncrypted, key+' '))