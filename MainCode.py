#Password contructor v1.0

class Password:
    def __init__(self, site, user, key, sep):
        self.site = site
        self.user = user
        self.key = key
        siteShort = ''.join([ele for ele in site if ele.isupper()])
        self.password = siteShort + sep + user + sep + key
MainArr = []

def Read():
    file = open('passwordsFile.txt', 'r')
    while True:
        Line = file.readline()
        if Line == "--E":
                break
        else:
            site, user, key, password = Line.split('+=+')
            MainArr.append(Password(site, user, key, password[-(len(key) + 2)]))

def Add():
    site = input('Type the site domain : \n')
    user = input('Type the username : \n')
    key = input('Type your special key (anything) : \n')
    sep = input('set the separator : \n')
    MainArr.append(Password(site, user, key))

def Remove():
    site = input('Type the site domain : \n')
    user = input('Type the username : \n')
    key = input('Type your special key : \n')
    for i in range(len(MainArr)):
        if MainArr[i].user == user:
            if MainArr[i].site == site:
                if MainArr[i].key == key:
                    Flag = input('Are you sure??(y/N) \n')
                    if Flag.lower() == 'y':
                        MainArr[i] = None
                        print('\n operation done!!! \n force stop to redo')

def QuitSequance():
    file = open('passwordsFile.txt', 'w')
    for i in range(len(MainArr)):
        if MainArr[i]:
            Txt = f'{MainArr[i].site}+=+{MainArr[i].user}+=+{MainArr[i].key}+=+{MainArr[i].password}\n'
            file.writelines(Txt)
    file.writelines('--E')
    return True

def Run():
    while True:
        qu = input('\n take a number \n 1 - Add Password \n 2 - Delete Password \n 3 - Quit \n')
        if qu == '1':
            Add()
        elif qu == '2':
            Remove()
        elif qu == '3':
            if QuitSequance() == True:
                break
        else:
            print("\n invalid input Try Again \n")



def StartUpSequance():
    print('Starting Up...')
    Read()
    Run()


StartUpSequance()
