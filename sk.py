from os import getcwdb
import os,sys
from posix import listdir
import socket,time
from getpass import getpass
#from pynput.keyboard import Key,Controller
name=open('user.txt','r').read()
passwd=open('passord.txt','r').read()
name_1=input('\033[1;33mEnter name: \033[1;35m')
passwd_1=getpass('\033[1;32mEntar passwd: \033[1;35m')

data=[]
if name_1 == name:
    a=1
    if passwd_1 == passwd:
        os.system('clear')
        print('''\n+ -- --=[ sekleton framwork v1.1.1-dev  ]
+ -- --=[ port scanig - payloads - exploits  ]   
+ -- --=[ exit - banner - help  ]''')
        while True:
            i=input(f'\n\033[1;34mSkeleton@\033[1;31m{name}\033[1;33m>\033[1;32m ')
            if i.startswith('sk -s'):
                a=0
                if i.startswith('sk -s'):
                    sd=i.strip('sk -s ')
                    HostToIP  = socket.gethostbyname(sd)
                    try:
                        import threading
                        def io():
                            print('    \033[1;31mportname    \033[1;36mportocol')
                            for port in range(1,89999):
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                sock.settimeout(0.5)
                                result = sock.connect_ex((HostToIP, port))
                                if result == 0:
                                    name_port=socket.getservbyport(port)
                                    #open port
                                    p=f'''\033[1;33mport    \033[1;32m{port}        \033[1;34m{name_port}'''
                                    print(p)
                        threading.Thread(target=io())
                    except Exception as erro:
                        print(erro)
            elif i.startswith('sk -m'):
                    HostToIP  = socket.gethostbyname('127.0.0.1')
                    try:
                        import threading
                        def io():
                            print('     \033[1;31mportname    \033[1;36mportocol')
                            for port in range(70,89999):
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                sock.settimeout(0.5)
                                result = sock.connect_ex((HostToIP, port))
                                if result == 0:
                                    name_port=socket.getservbyport(port)
                                    #open port
                                    p=f'''\033[1;33mport    \033[1;32m{port}        \033[1;34m{name_port}'''
                                    print(p)
                        threading.Thread(target=io())
                    except Exception as erro:
                        print(erro)
            elif i.startswith('sk -u and p'):
                skl=i.strip('sk -p')
                name_2=input('Enter new name: ')
                passwd_2=input('Entar new passwd: ')
                open('user.txt','w').write(name_2)
                open('passord.txt','w').write(passwd_2)
            elif i.startswith('ls'):
                ls=i.strip('ls')
                a=listdir()
                for i in a:
                    print(i)
            elif i.startswith('pwd'):
                pwd=i.strip('pwd')
                print(getcwdb())
            elif i.startswith('sk -build star[1] -p 4444 -python exe -name'):
                b=i.strip('sk -build star[1] -p 4444 -python exe -name ')
                def D():
                    build=open('.build','rb').read()
                    st=f'\033[1;34m[*]\033[1;32mDone install build python port 80 name {b}\n'
                    for j in st:
                        sys.stdout.write(j)
                        sys.stdout.flush()
                    install=open(st,'wb').write(build)
                    print('Done...............[*]')
                D()
            elif i.startswith('cd'):
                cd=i.strip('cd ')
                try:
                    if os.path.exists(cd):
                        os.chdir(cd)
                    else:
                        a=f'{cd}: file not found'
                        print(a)
                except FileNotFoundError as f:
                    print(f)
    else:
        print('Incorrect password')
else:
    print('the name is incorrect')
