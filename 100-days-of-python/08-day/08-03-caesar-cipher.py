def ceacerCipher(action, message, shift_step):
    new_message = ""
    if action == "decode":
        shift_step = -1 * shift_step

    for i in range(0, len(message)):
        if message[i] in alphabet:
            new_message_index = alphabet.index(message[i]) + shift_step
            if new_message_index >= len(alphabet):
                new_message_index = new_message_index - (len(alphabet))
            elif (new_message_index < 0 ):
                new_message_index = (len(alphabet)) + new_message_index
            message[i] = alphabet[new_message_index]
            new_message += message[i]
        else:
            print("isNotInList")
    print(str(new_message))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', \
    '!', '@', '.', ',', ':', '_', '?', ';', '-', '"', '\'', '`']

action = input("Encode or Decode message?(encode, decode): ")
message = list(input("Your message: "))
shift_step = int(input("shift: "))
ceacerCipher(action, message, shift_step)
