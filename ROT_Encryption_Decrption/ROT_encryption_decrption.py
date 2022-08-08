import os
import sys
import time

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceasr(text,shift,method):
    final_text=""
    if method == 2:
        shift = -1
    for letter in text:
        if letter in alpha:
            position = alpha.index(letter)
            pos = position + shift
            e_position = pos % 26
            new_word = alpha[e_position]
            final_text += new_word
        else:
            final_text += letter
    return final_text 

def main():
    print("Enter 1 : Encode")
    print("Enter 2 : decode")
    method=int(input("Enter Your Choice : "))
    text=input("Enter Your Message in Lower Case : ").lower()
    shift=int(input("Enter Your Shift/key : "))
    if method == 1:
        msg="Encoded"
    else:
        msg="Decoded"
    os.system('cls')
    a=ceasr(text,shift,method)
    print("WAIT FOR A WHILE........ ")
    time.sleep(2)
    os.system('cls')
    print("YOUR MESSAGE IS GETTING ENCRYPTING OR DECRYPTING................. ")
    time.sleep(2)
    os.system('cls')
    print("------------------------------")
    print(f"This Message is {msg} : {a}")
    print("------------------------------\n")

    print("Do You want To Encode or Decode Any Message.")
    rev=input("Press Y or y to Contine or press any key to Exit : ")
    if rev == 'y' or rev =='Y':
        os.system('cls')
        main()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
