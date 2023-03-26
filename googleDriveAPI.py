from myLib import display_and_load_first_ten
from myLib import download
from myLib import account_info
from myLib import fileToID

def main():
    print("**********Google Drive API**********")
    account_info()
    print("First 10 files are as follows: \n")
    display_and_load_first_ten()
    name = input("File to be downloaded\n")
    if name in fileToID:
        download(fileToID[name], name)
    else:
        print("No such file")

if __name__ == '__main__':
    main()