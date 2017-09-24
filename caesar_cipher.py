message=input("Enter message: ")
key=int(input("Enter key: "))
#a_list=letter.split()
def encrypt(message,key):
    final_word=""
    for char in message:
        if char.isalpha():
            charcode=ord(char)
            charcode+=key
            if char.isupper():
                if charcode>ord("Z"):
                    charcode-=26
                if charcode<ord("A"):
                    charcode+=26
            else:
                if charcode > ord("z"):
                    charcode -= 26
                if charcode < ord("a"):
                    charcode += 26
            final_word+=chr(charcode)
        else:
            final_word+=char
    return final_word

print(encrypt(message,key))
key_new=-key
print(encrypt(encrypt(message,key),key_new))