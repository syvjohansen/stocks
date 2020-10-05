##Step one is to get the Russell 3000

#import PyPDF2

#Open the PDF
#pdfFileObj = open('russell-3000-membership.pdf', 'rb')

#get s&p 500 company list
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlsxwriter
from xlutils.copy import copy    
from xlrd import open_workbook


sp_wiki = ('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
sp_wiki = urlopen(sp_wiki)
sp_soup = BeautifulSoup(sp_wiki, 'html.parser')

index = []
sector = []
subsector = []
peg = []


'''
for a in range(len(sp_soup.find_all('td'))):
#for a in range(10):
	if(a%9==0):
		ticker = (sp_soup.find_all('td')[a].get_text())
		print(ticker)
'''
#This gets the tickers from the S&P
num=0
for a in (sp_soup.find_all('a', {"class": "external text"})):
	if(len(a.get_text())>7):
		break
	if(num%2==0):
		index.append(a.get_text())
	num = num+1



#print(td)

#This one gets the sectors from the S&P

sp_tr = sp_soup.find_all('tr')
#for a in range(len(sp_tr)):
for a in range(1, (len(sp_tr))):
	try:
		sp_td = sp_tr[a].find_all('td')
		sector.append(sp_td[3].get_text())
		subsector.append(sp_td[4].get_text())
	except:
		break

	#print(sp_tr[a].get_text())

#Now we get the PEG for each ratio from Zack's
#for a in range(len(index)):
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
#urlopen('https://www.zacks.com/')
#urlopen('https://www.zacks.com/stock/quote/AAPL')
workbook = open_workbook("/Users/syverjohansen/stocks/scrapes/peg.xls")
book = copy(workbook)
sheet = book.get_sheet(0)

peg_start = 0

#for a in range(len(index)):
try:
	for a in range(505, len(index)):
		
		#print(str(index[a]))
		ind_zack = 'https://www.zacks.com/stock/quote/'+str(index[a])
		r = urllib.request.Request(ind_zack, headers=header)
		with urllib.request.urlopen(r) as response:
			the_page = response.read()
		#print(the_page)
		zack_soup = BeautifulSoup(the_page, 'html.parser')
		zack_sect = zack_soup.find_all("section", {"id": "stock_key_earnings"})
		zack_sect = zack_sect[0]
		zack_td = zack_sect.find_all("td")
		if(zack_td[-2].get_text() == "PEG Ratio"):
			peg.append(zack_td[-1].get_text())
		else:
			peg.append("NA")
		sheet.write(a, 0, index[a])
		sheet.write(a, 1, sector[a])
		sheet.write(a, 2, subsector[a])
		sheet.write(a,3,peg[peg_start])
		peg_start = peg_start+1
		print(a)
	book.save("/Users/syverjohansen/stocks/scrapes/peg.xls")
except:
	book.save("/Users/syverjohansen/stocks/scrapes/peg.xls")
print(peg)
print(len(peg))

