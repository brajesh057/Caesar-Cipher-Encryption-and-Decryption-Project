alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(direction,text, shift):
     caesar_capler=''
     if direction=="encode":
        for word in text:
            if word in alphabet:
                position=alphabet.index(word)
                y=position+shift
                encrypted_text=(alphabet[y])
                caesar_caplere+=encrypted_text
        print(caesar_caplere)
     if direction=="decode":
        caesar_caplerd=''
        for word in text:
            if word in alphabet:
                position=alphabet.index(word)
                y=position-shift
                dencrypted_text=(alphabet[y])
                caesar_caplerd+=dencrypted_text
        print(caesar_caplerd)        

    
encrypt(direction,text,shift)
