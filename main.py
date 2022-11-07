def encode(password):
    global encoded_pass
    encoded_pass = ""
    for i in range(pass_length):
        digit = str(int(password[i])+3)
        encoded_pass += digit
    return encoded_pass

def decode(encoded_pass):
    decoded_pass = ""
    for i in range(pass_length):
        digit = str(int(encoded_pass[i])-3)
        decoded_pass += digit
    return decoded_pass

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    oper = int(input("Please enter an option: "))
    if oper == 1:
        global password
        password = str(input("Please enter your password to encode: "))
        pass_length = len(password)
        print("Your password has been encoded and stored!")
        print(encode(password))
        True
    elif oper == 2:
        print("The encoded password is ", encoded_pass, " and the original password is ",decode(encoded_pass))
        True
    elif oper == 3:
        quit()
