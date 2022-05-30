import ceasar_art

print(ceasar_art.logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(shift):
#     for n in range(0, space):
#         b = alphabet.index(text_list[n])
#         e_shift = b + shift
#         if e_shift>=25:
#             e_shift = e_shift - 26
#             text_list[n] = alphabet[e_shift]
#         else:
#             text_list[n] = alphabet[e_shift]
#
#     cipher_text = ''.join(text_list)
#     print(f"The encoded text is {cipher_text}")
#
# def decrypt(shift):
#   for n in range(0, space):
#       b = alphabet.index(text_list[n])
#       text_list[n] = alphabet[b-shift]
#
#   plain_text = ''.join(text_list)
#   print(f"The encoded text is {plain_text}")

def caesar(shift, direction):
    if direction == "encode":
        for n in range(0, space):
            if text_list[n] in alphabet:
                b = alphabet.index(text_list[n])
                e_shift = b + shift
                if e_shift>=25:
                    while not e_shift<=25:
                        e_shift = e_shift - 26
                    text_list[n] = alphabet[e_shift]
                else:
                    text_list[n] = alphabet[e_shift]

        cipher_text = ''.join(text_list)
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        for n in range(0, space):
            if text_list[n] in alphabet:
                b = alphabet.index(text_list[n])
                text_list[n] = alphabet[b-shift]
        plain_text = ''.join(text_list)
        print(f"The encoded text is {plain_text}")
    else:
        print("Invalid Response")

repeat = True

while repeat == True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text_list = list(text)
        space = len(text)

        caesar(shift, direction)

        result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()

        if result == 'no':
            repeat = False
            print("Goodbye")


