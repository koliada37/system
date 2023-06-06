import os
import Enc

userRoles = {
    "user1": "user",
    "user2": "user",
    "user3": "admin",
    "admin": "admin"
}
namePass = {
    "user1": "111",
    "user2": "222",
    "user3": "333",
    "admin": "admin"
}
def UsrPassRole(currUser):
    def checkName(name):
        global passw
        passw=str(input("Enter pass: "))
        if name in userRoles:
            return(checkPass(name,passw))
        else:
            print('Login FAILED')
            return('err')

    def checkPass(name,passw):
        if namePass[name] == passw:
            print('SECCES login as', name)
            return (checkRole(currUser))
        else:
            print('Login FAILED')
            return('err')

    def checkRole(name):
        if name in userRoles:
            print('Role:', userRoles[name])
            return userRoles[name]
        else:
            return('err')


    return(checkName(currUser))

userInputed=str(input("Enter username: "))
LogStatus=UsrPassRole(userInputed)
global passw
while 0 != 2:
    if (LogStatus == 'user'):
        print('$:: ')
        inpUsr = input()
        if inpUsr == 'enc':
            print(inpUsr, passw, userInputed)
            Enc.Enc(passw,userInputed)
        elif inpUsr == 'dec':
            Enc.Dec(passw,userInputed)
        else:
            print(os.system(inpUsr))
    elif (LogStatus == 'admin'):
        print('$:: ')
        inpUsr = input()
        if inpUsr == 'enc':
            adminTryAccess = input('Which user you wanna access? ')
            Enc.Enc(namePass[adminTryAccess],adminTryAccess)
        elif inpUsr == 'dec':
            adminTryAccess = input('Which user you wanna access? ')
            Enc.Dec(namePass[adminTryAccess],adminTryAccess)
        else:
            print(os.system(inpUsr))
    else:
        break
