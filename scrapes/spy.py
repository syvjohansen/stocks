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


def RemoveIthWord(lst, word, N): 
    newList = [] 
    count = 0
  
    # iterate the elements 
    for i in lst: 
        if(i == word): 
            count = count + 1
            if(count != N): 
                newList.append(i) 
        else: 
            newList.append(i) 
              
    lst = newList 
      
    if count == 0: 
        print("Item not found") 
    else: 
        print("Updated list is: ", lst)     
      
    return newList 
  
# Driver code 



def get_date(script):
	date_1 = datetime.datetime.strptime("1/1/70", "%m/%d/%y")
	date_word = ['date']
	date = scripts
	date[:] = [num for num in date if any(sub in num for sub in date_word)]
	date = "".join(date)
	date = (date.split("\"date\":"))
	date = date[1:]
	#print(date)
	for i in range(len(date)):
		date[i] = int(str(date[i]))
	date = [math.floor(x/60/60/24) for x in date]
	date = [date_1 + datetime.timedelta(days=x) for x in date]
	date = [datetime.datetime.date(x).strftime('%m/%d/%y') for x in date] 
	print('09/18/20' in date)
	divs_date = ['09/18/20', '06/19/20', '03/20/20', '12/20/19']
	for a in divs_date:
		date = RemoveIthWord(date, a, 2)
	return date

def get_opens(script):
	opens_word = ['open']
	opens = scripts
	#print(opens)
	opens[:] = [num for num in opens if any(sub in num for sub in opens_word)]
	opens = "".join(opens)
	opens = (opens.split("\"open\":"))
	opens = opens[1:]
	#print(opens)
	for i in range(len(opens)):
		opens[i] = float(str(opens[i]))
	return opens

spyahoo = 'https://finance.yahoo.com/quote/SPY/history/'
spyahoo = urlopen(spyahoo)
spyoup = BeautifulSoup(spyahoo, 'html.parser')

scripts = (spyoup.find_all("script"))

scripts = (scripts[52])
scripts=str(scripts)
scripts = scripts.split("HistoricalPriceStore\":{\"prices\":")
scripts = scripts[1]
scripts = scripts.split(",\"isPending\":false,\"firstTradeDate")
scripts = (scripts[0])
scripts = scripts.split("[")
scripts = scripts[1]
scripts = scripts.split("]")
scripts = scripts[0]
scripts = scripts.replace('{', '')
scripts = scripts.replace('}', '')
scripts = scripts.split(',')
scripts_copy = copy.deepcopy(scripts)

#print(scripts2)

'''date_word = ['date']
date = scripts
date[:] = [num for num in scripts if any(sub in num for sub in date_word)]
date = "".join(date)
date = (date.split("\"date\":"))
date = date[1:]
#print(date)
for i in range(len(date)):
	date[i] = int(str(date[i]))'''


date = get_date(scripts)
scripts = scripts_copy
print(scripts)
opens = get_opens(scripts)
print(len(date))
print(len(opens))




#print(date)	

print(date)
print(opens)


opens_word = ['open']
opens = scripts
#print(opens)
opens[:] = [num for num in scripts if any(sub in num for sub in opens_word)]
opens = "".join(opens)
opens = (opens.split("\"open\":"))
opens = opens[1:]
#print(opens)
for i in range(len(opens)):
	opens[i] = float(str(opens[i]))
#print(opens)

workbook = open_workbook("/Users/syverjohansen/stocks/scrapes/spy.xls")
book = xcopy(workbook)
sheet = book.get_sheet(0)

for a in range(len(date)):
	try:
		sheet.write(a, 0, date[a])
		sheet.write(a, 1, opens[a])
	except:
		continue

book.save("/Users/syverjohansen/stocks/scrapes/spy.xls")



#print(date)

#date_scripts = scripts.split('\"date\":')
#print(date_scripts[1])



'''for a in range(53, 1525)
span = spyoup.find_all('span', {'data-reactid': '53'})
print(span[1])'''

