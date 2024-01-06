import string
import random
#ask user to specify password length
length=int(input("Please enter the desired length of password: "))
print("Choose character set for password")
print('|--------------------------|')
print('|     1.Digits             |')
print('|     2.Letters            |')
print('|     3.Special character  |')
print('|     4.Exit               |')
print('|--------------------------|')
charList=" "
while(True):
    choice=int(input('Pick a number: '))
    if(choice == 1):
        charList +=string.digits          #for digits
    elif(choice == 2):
        charList +=string.ascii_letters   #for letters
    elif(choice == 3):
        charList +=string.punctuation     #for special character
    elif(choice == 4):
        break
    else:
        print('Please pick a valid option!')
pwd=[]
for i in range (length):
    randomC=random.choice(charList)
    pwd.append(randomC)
print('The random password is '  + "".join(pwd))
        
