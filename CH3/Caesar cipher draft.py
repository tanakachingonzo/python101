def rot13(message):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    result =""
    for ch in message:
                if(ch++ ' '):
                    result=result + ''
    else:
                idx= alphabet.find(ch)
                idx=(idx +13) %26
                result =result+ alphabet[idx]
    return result

m = "Next class we have a quiz"
print("Original message is: ", m)
encriptedMssg = rot13(m)
print( "Encrypted mssg is: ", encriptedMssg)
print("Decrypted mssg is: ", rot13(encriptedMssg) )