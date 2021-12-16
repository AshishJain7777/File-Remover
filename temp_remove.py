## Ashish Jain :: December - 16 - 2021
# Permanent File Removing Program
username = ['admin','developer']
password = ['ap1234','1234']
note = 'This Program Will Clear Your All Unnecessary Chace And Temporary Files:::::  '
gif = '''

           _          _    ._____________.
          | |        | |   |_____   _____|   
          | |________| |        |   |
          | |________| |        |   |
          | |        | |        |   |  
          | |        | |    ____|   |____
          |_|        |_|   |_____________|



      '''
print(note)
print(gif)
while True:
    user = input('Please Enter Username: ')
    if user ==  username[0]:
        enter = user
        break
    elif user ==  username[1]:
        enter = user
        break
    else:
        print('Please Enter A Valid Username')

while True:
    passkey = input('Please Enter Password: ')
    if enter == username[0] and passkey == password[0]:
        main = 'admin'
        break
    elif enter == username[1] and passkey == password[1]:
        main = 'developer'
        break
    else:
        print('Password Mismatch Try Again',enter)
while True:
    if main == username[0]:
        filename = input('Please Enter File Name You Want To Remove Permanently From Your System: ')
        if filename.lower() == 'done':
            exit()
        else:
            try:
                import os
                os.remove(filename)
                print('File Removed Succesfully')
                continue
            except:
                print('Permission Denied. Make Sure To Put Extension Of The Given File. Ex: "temp.txt" ')
                break
    elif main == username[1]:
        print('You Have No Access To Remove Anything From System ')
        break