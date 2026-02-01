from getpass import getpass 
password =getpass("enter password: ")

while password: 
    if password<='9999':
        break
    else:
        exit("Eror, your password is very long OR You did not enter a number!")

        
chance = (input("try your chance: "))
while chance: 
    if chance<='999':
        break
    else:
        exit("Eror, your password is very long OR You did not enter a number!")
        
while password!=chance:
    chance=input("is not true password, plase try again: ")

print("Your lucky")

