
from art import art
import string 
from timeit import timeit



def cryptography(option, text, key=0):
    """
        This funtion encrypt or decrypt a text based on the given key 
    """
    print(art)
    lowerCase = string.ascii_lowercase
    encrypt = []
    try:
        for chr in text: 
            if chr in lowerCase:
                index = lowerCase.index(chr)
                if option == '1':
                    lowerCase = lowerCase + lowerCase[: key + 1]
                    encrypt.append(lowerCase[index+ key])
                else:
                    lowerCase = lowerCase[-1: -key] + lowerCase
                    encrypt.append(lowerCase[index - key])
            else: 
                encrypt.append(chr)
    except (IndexError, ValueError):
        print('Out of Index')
    finally:
        return ' '.join(encrypt)

# "TESTING FOR TIME COMPLEXITY"
# option = '1'
# text = "Nothinig inthe world to stop 112 in the la for sure"
# key = 5
# result = timeit(lambda: cryptography(option, text, key), number = 1)
# print(result)


while True: 
    key = 0
    options = {'1': 'ENCODE', '2': 'DECODE'}
    option = input("What would like to do? \n\t 1. Encrypt \n\t 2. Decrypt \n\t  choose 1 to encrypt or 2 to decrypt ")
    if option not in options.keys():
        print("Invalid Option")
        break
    text = input(f"Enter the text you want to {options[option]}: \n\t")
    try:
        key = int(input("Enter Key: "))
    except ValueError:
        while not key:
            validKey = input("Enter a valid key: \n\tpress q to quit: ")
            print('key must be an integer less than 25')
            if validKey == 'q':  break
            elif validKey.isdigit() and int(validKey) < 25: key = int(validKey); break
            else: 
                continue

    text_output = cryptography(option, text, key)
    print(text_output, end = '\n\n')
    response = input("Do you want to continue? y/n: \n")
    if response == 'n':

        print("\n\tTHANK YOU FOR USING THE CRYPTO SERVICE\n")

        break
