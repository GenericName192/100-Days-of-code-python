alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run = True

def encrypt(text, shift):
    encodedText = ""
    for charcter in text:
        if charcter not in alphabet:
            encodedText += charcter
        else:
            letterIndex = alphabet.index(charcter) + shift
            while letterIndex >= len(alphabet):
                letterIndex = letterIndex % len(alphabet)
            encodedText += alphabet[letterIndex]
    return encodedText

def decrypt(text, shift):
    decodedText = ""
    for charcter in text:
        if charcter not in alphabet:
            decodedText += charcter
        else:
            letterIndex = alphabet.index(charcter) - shift
            while letterIndex < 0:
                letterIndex += len(alphabet)
            decodedText += alphabet[letterIndex]
    return decodedText

def caesar(startText, shift_number, cipher_direction):
    if cipher_direction != "encode" and cipher_direction != "decode":
        return "Invalid direction"
    endText = ""
    for charcter in startText:
        if charcter not in alphabet:
            endText += charcter
        else:
            if cipher_direction == "encode":
                letterIndex = alphabet.index(charcter) + shift_number
                if letterIndex >= len(alphabet):
                    letterIndex = letterIndex % len(alphabet)
                endText += alphabet[letterIndex]
            else:
                letterIndex = alphabet.index(charcter) - shift_number
                if letterIndex < 0:
                    letterIndex = letterIndex % len(alphabet)
                endText += alphabet[letterIndex]           
    return endText


while run:

    direction = input("Type (encode) to encrypt, type (decode) to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(startText = text, shift_number = shift, cipher_direction = direction))


    endProgram = input("Do you want to do something else? (yes) (no) \n").lower()
    if endProgram == "no":
        run = False



