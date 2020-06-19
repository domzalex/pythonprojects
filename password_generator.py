import random
import string

yn = ["yes", "no"]
strong = 0
complex = 0

while True :

    passchar = input('How many characters do you want your password to contain? Enter 0 to quit. ')
    passlen = int(passchar)
    if passlen < 1 :
        break

    if passlen < 6 :
        print('Too few password characters. Please choose a minimum of 6.')
        continue



    strength = input('Do you want a mix of letters and numbers? Enter "no" for only letters. ')
    if not strength in yn :
        print('Invalid entry. Enter "yes" or "no".')
        continue

    if strength == "yes" :
        strong = 1



    complexity = input('Do you want your password to contain special characters? ')
    if not complexity in yn :
        print('Invalid entry. Enter "yes" or "no".')
        continue

    if complexity == "yes" :
        complex = 1



    def passwordgen1(len=passlen):
        passchar = string.ascii_letters
        return ''.join(random.choice(passchar) for i in range(len))

    def passwordgen2(len=passlen):
        passchar = string.ascii_letters + string.digits
        return ''.join(random.choice(passchar) for i in range(len))

    def passwordgen3(len=passlen):
        passchar = string.ascii_letters + string.punctuation
        return ''.join(random.choice(passchar) for i in range(len))

    def passwordgen4(len=passlen):
        passchar = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(passchar) for i in range(len))



    print("Your generated password: ")
    if strong == 0 and complex == 0 :
        print(passwordgen1())
        break
    elif strong == 1 and complex == 0 :
        print(passwordgen2())
        break
    elif strong == 0 and complex == 1 :
        print(passwordgen3())
        break
    elif strong == 1 and complex == 1 :
        print(passwordgen4())
        break
