import os
def main():
    ask = input("what's the file's path: ")
    cord = input('create or delete: ')
    nm = input('name of the file: ')
    detect = os.path.exists(os.path.join(ask, nm))
    if detect == True:
        truepath = os.path.join(ask, nm)
        if cord == "delete" or cord == "Delete" or cord == "Del" or cord == "del":
            os.remove(truepath)
            print('file deleted.')
        elif cord == "create" or cord == "Create":
            file = open(truepath, 'w')
            print('file created!')
        else:
            print('uhh what? please try again??')
            main()
    else:
        print('invalid path.')
        main()
main()
