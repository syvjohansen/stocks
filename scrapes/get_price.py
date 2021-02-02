import pandas as pd
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlsxwriter
import xlutils
from xlutils.copy import copy as xcopy   
from xlrd import open_workbook
import re
import copy
import math
import datetime 
from datetime import timedelta


header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
#urlopen('https://www.zacks.com/')
#urlopen('https://www.zacks.com/stock/quote/AAPL')
df2 = pd.DataFrame()#columns = ['Asset', 'Price'])
df2.to_excel("/Users/syverjohansen/stocks/scrapes/get_price.xls")
workbook = open_workbook("/Users/syverjohansen/stocks/scrapes/get_price.xls")
book = xcopy(workbook)
sheet = book.get_sheet(0)

open_price = []
peg = []
df = pd.read_excel(r'/Users/syverjohansen/stocks/portfolio/my_portfolio.xlsx')



for a in range(1, len(df[df.columns[0]])):
	
	#print(a)
	print(df[df.columns[0]][a])
	ind_zack = 'https://www.zacks.com/stock/quote/'+str(df[df.columns[0]][a])
	r = urllib.request.Request(ind_zack, headers=header)

	with urllib.request.urlopen(r) as response:
		the_page = response.read()
	
	zack_soup = BeautifulSoup(the_page, 'html.parser')
	try:
		zack_sect = zack_soup.find_all("div", {"class":"two_col"})
		#print(zack_sect[0])
		zack_sect = zack_soup.find_all("dd")
		zack_sect = (zack_sect[0].get_text())
		zack_sect = zack_sect.replace(",","")
		try:
			open_price.append(float(zack_sect))
		except:
			open_price.append("NA")
		#print(zack_td[1])
		zack_peg = zack_soup.find_all("dd")
		zack_peg = zack_peg[17]
		try:
			zack_peg = (zack_peg.get_text())
			peg.append(float(zack_peg))
		except:
			peg.append("NA")
		
		sheet.write(a, 0, df[df.columns[0]][a])
		sheet.write(a, 1, open_price[a-1])
		sheet.write(a, 2, peg[a-1])
	except:
		zack_sect = zack_soup.find_all("section", {"id": "etf_quote_details"})
		zack_sect = zack_sect[0]
		zack_td = zack_sect.find_all("td")
		#print(zack_td[2])
		if(zack_td[2].get_text() == "Open"):
			
			open_price.append(float(zack_td[1].get_text().replace(',','')))
			#print(zack_td[1].get_text())
		else:
			open_price.append("NA")
		if(zack_td[-2].get_text() == "PEG Ratio"):
			peg.append(zack_td[-1].get_text())
		else:
			peg.append("NA")
	#	print(open_price)
		sheet.write(a, 0, df[df.columns[0]][a])
		sheet.write(a, 1, open_price[a-1])
		sheet.write(a, 2, "NA")
		

	
	
book.save("/Users/syverjohansen/stocks/scrapes/get_price.xls")



