import os
print('please put the FULL path for example: \n instead of: c:/tfolder \n do: c:/tfolder/tfile.txt')
ask = input("what's the file's name/path: ")
cord = input('create or delete: ')
if cord == "delete":
    os.remove(ask)
    print('file deleted.')
if cord == "create":
    file = open(ask, 'w')
    print('file created!')
