import pyAesCrypt
import glob
import os
def Dec(password1, encFile):
    bufferSize = 64 * 1024
    curDir = os.getcwd()
    print('\n> Beginning recursive decryption...\n\n')
    encFile = './FS/'+encFile+'/**/*'
    for x in glob.glob(encFile, recursive=True):
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, os.path.splitext(x)[0])
        if os.path.isfile(fullpath):
            print('>>> Encrypted: \t' + fullpath + '')
            try:
                pyAesCrypt.decryptFile(fullpath, fullnewf, password1, bufferSize)
                print('>>> Decrypted: \t' + fullnewf + '\n')
                os.remove(fullpath)
            except ValueError:
                print('>>> Error - Wrong password!\n')

def Enc(password1, encFile):
    bufferSize = 64 * 1024
    curDir = os.getcwd()
    print('\n> Beginning recursive encryption...\n\n')
    encFile = './FS/'+encFile+'/**/*'
    print(encFile)
    for x in glob.glob(encFile, recursive=True):
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, x + '.aes')
        if os.path.isfile(fullpath):
            print('>>> Original: \t' + fullpath + '')
            print('>>> Encrypted: \t' + fullnewf + '\n')
            pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
            os.remove(fullpath)