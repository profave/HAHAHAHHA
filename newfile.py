#!/usr/bin/python3
# 𝗗𝗼𝗻'𝘁 𝗳𝗼𝗿𝗴𝗲𝘁 𝘁𝗼 𝗳𝗼𝗹𝗹𝗼𝘄 𝗺𝘆 𝗴𝗶𝘁𝗵𝘂𝗯 𝗼𝗸
# 𝗴𝗶𝘃𝗲 𝗮 𝘀𝘁𝗮𝗿 𝘁𝗼 𝘁𝗵𝗲 𝗿𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆 𝘁𝗵𝗮𝘁 𝗜 𝗰𝗿𝗲𝗮𝘁𝗲𝗱
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64,uuid
from datetime import datetime
from time import sleep
ses=requests.Session()

ua1 = "Mozilla/5.0 (Linux; Android 10; Wildfire E Lite Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]"
ua2 = "Mozilla/5.0 (Linux; Android 11; KINGKONG 5 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/320.0.0.12.108;]"
ua3 = "Mozilla/5.0 (Linux; Android 11; G91 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/325.0.1.4.108;]"
ua = random.choice([ua1,ua2,ua3])

def login():
	os.system("clear")
	print("masukan cookie Facebook")
	cookie = input(f"cookie : ")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent":ua,"referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		to = open("token.txt","r").read()
		print("\ntoken : "+to);time.sleep(1)
		bot()
	except:
		os.system("rm token.txt ")
		os.system("rm cookie.txt")
		print("login Failed the cookie expired")
		login()

def bot():
	os.system('clear')
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}	    
	except:
		os.system("rm token.txt")
		os.system("rm cookie.txt")
		print("cookie kadalwarsa")
		login()
	os.system('clear')
	link = input(f"link postingan : ")
	jumlah = int(input(f"jumlah : "))
	print("ꜱʜᴀʀᴇ ᴘʀᴏᴄᴇꜱꜱ ɪꜱ ʀᴜɴɴɪɴɢ ᴘʀᴇꜱꜱ ᴄᴛʀʟ + ᴢ ᴛᴏ ꜱᴛᴏᴘ")
	RianGantengBanget = datetime.now()
	try:
		n = 0
		header= {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":ua}
		for x in range("Eɴᴛᴇʀ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ꜱʜᴀʀᴇꜱ"):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				rianxd = str(datetime.now()-RianGantengBanget).split('.')[0]
				print(f'*——> {n}.berhasil share\n',end='');sys.stdout.flush()
			else:
				print("\n")
				pritn("Share berhenti kemungkinan cookie atau tumbal di tangguhkan")
	except requests.exceptions.ConnectionError:
		print(f"\n(!) ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ!");exit()

bot()
