#CODED BY MR QURESHI <3 
#OPEN SOURCE CODE FOR WEB SCRAPING OF QURAN-PAK SURAH <3
import re,requests,bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()
no,surat,name_surat=0,[],[]

url = parser(ses.get("https://litequran.net/").text,"html.parser")
for data in url.find_all("a",href=True):
	name_surat.append(data.text)
	if "https://Litequran.net/" in data.get("href"):
		pass
	else:
		if "Privacy Policy" in data.text:
			pass
		else:
			no +=1
			print(f"{no}. {data.text}")
			surat.append(data.get("href"))

ask = input("\n [-] ENTER DIGITS : ")
url2 = parser(ses.get(f"https://litequran.net/{surat[int(ask)-1]}").text,"html.parser")
for det in url2.find_all("p",{"class": ["arabic","translate"]}):
	print(det.text)
