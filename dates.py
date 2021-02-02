import datetime
from datetime import date

today = datetime.datetime.now()


#AMD
d1 = datetime.datetime(2016, 3, 8, 0,0,0)
d2= datetime.datetime(2017, 10, 23, 0,0,0)
d3= datetime.datetime(2020, 6, 15, 0,0,0)
d4= datetime.datetime(2020, 8, 7, 0,0,0)
d5= datetime.datetime(2020, 8, 10, 0,0,0)
d6= datetime.datetime(2020, 8, 24, 0,0,0)
d7= datetime.datetime(2020, 9, 1, 0,0,0)
d8=datetime.datetime(2020, 9, 16, 0,0,0)
d9=datetime.datetime(2020, 11, 1, 0,0,0)

print("AMD "+ str(((today-d1).days*12+(today-d2).days*5+(today-d3).days*5+(today-d4).days*10
	+(today-d5).days*10+(today-d6).days*7+(today-d7).days*1.081549+(today-d8).days*.036672+
	(today-d9).days*3.965137)/54.083358))


d1 = datetime.datetime(2016, 2, 12, 0,0,0)
d2= datetime.datetime(2016, 2, 23, 0,0,0)
d3= datetime.datetime(2017, 5, 5, 0,0,0)
d4= datetime.datetime(2020, 8, 11, 0,0,0)
d5= datetime.datetime(2020, 8, 24, 0,0,0)
d6= datetime.datetime(2020, 8, 25, 0,0,0)
d7= datetime.datetime(2020, 9, 1, 0,0,0)
d8=datetime.datetime(2020, 9, 16, 0,0,0)
d9 = datetime.datetime(2021, 1, 16, 0,0,0)
d10 = datetime.datetime(2021, 1, 16, 0,0,0)
print("BABA "+ str(((today-d1).days*1+(today-d2).days*1+(today-d3).days*5+(today-d4).days*4
	+(today-d5).days*1.694136+(today-d6).days*.260491+(today-d7).days*.344934+
	(today-d8).days*.060534+(today-d9).days*1+(today-d10).days*3)/17.360095))

d1 = datetime.datetime(2016, 2, 19, 0,0,0)
d2= datetime.datetime(2016, 2, 23, 0,0,0)
d3= datetime.datetime(2016, 3, 8, 0,0,0)
print("FB "+ str(((today-d1).days*2+(today-d2).days*1+(today-d3).days*10)/13))


d1 = datetime.datetime(2020, 8, 20, 0,0,0)
d2= datetime.datetime(2020, 9, 1, 0,0,0)
print("IGV "+ str(((today-d1).days*2+(today-d2).days*.306706)/2.306706))

d1 = datetime.datetime(2020, 9, 23, 0,0,0)
d2= datetime.datetime(2020, 9, 25, 0,0,0)
d3= datetime.datetime(2020, 9, 30, 0,0,0)
d4 = datetime.datetime(2020, 12, 28, 0,0,0)
print("LIT "+ str(((today-d1).days*13.384771+(today-d2).days*.051391+(today-d3).days*.371732+(today-d4).days*2.467145)/16.275039))


d1 = datetime.datetime(2020, 8, 11, 0,0,0)
d2= datetime.datetime(2020, 8, 28, 0,0,0)
d3= datetime.datetime(2020, 9, 1, 0,0,0)
print("MSFT "+ str(((today-d1).days*5+(today-d2).days*.205137+(today-d3).days*.443862)/5.648999))

d1 = datetime.datetime(2016, 10, 17, 0,0,0)
d2= datetime.datetime(2020, 9, 14, 0,0,0)
print("NFLX "+ str(((today-d1).days*1+(today-d2).days*.014446)/1.014446))

d1 = datetime.datetime(2015, 12, 24, 0,0,0)
d2= datetime.datetime(2020, 6, 15, 0,0,0)
d3= datetime.datetime(2020, 8, 7, 0,0,0)
print("NVDA "+ str(((today-d1).days*1+(today-d2).days*5+(today-d3).days*5)/12))

d1 = datetime.datetime(2020, 8, 24, 0,0,0)
d2= datetime.datetime(2020, 9, 18, 0,0,0)
print("TCEHY "+ str(((today-d1).days*15+(today-d2).days*.031708)/15.031708))

d1 = datetime.datetime(2020, 8, 10, 0,0,0)
d2= datetime.datetime(2020, 8, 11, 0,0,0)
d3= datetime.datetime(2020, 8,21, 0,0,0)
d4= datetime.datetime(2020, 8, 31, 0,0,0)
d5= datetime.datetime(2020, 9, 1, 0,0,0)
print("TSLA " + str(((today-d1).days*5+(today-d2).days*5+(today-d3).days*5*.512678+(today-d4).days*.028289
	+(today-d5).days*.203035)/12.794714))

d1 = datetime.datetime(2020, 9, 10, 0,0,0)
d2= datetime.datetime(2020, 10, 1, 0,0,0)
print("MU "+ str(((today-d1).days*11.01335+(today-d2).days*.219088)/11.232438))

d1 = datetime.datetime(2020, 8, 26, 0,0,0)
d2= datetime.datetime(2020, 10, 12, 0,0,0)
print("NOC "+ str(((today-d1).days*1.464131+(today-d2).days*.446057)/1.910188))

d1 = datetime.datetime(2020, 9, 2, 0,0,0)
d2= datetime.datetime(2020, 11, 1, 0,0,0)
d3 = datetime.datetime(2020, 12, 1, 0,0,0)
print("ZM "+ str(((today-d1).days*.238962+(today-d2).days*.021996+(today-d3).days*.607518)/0.868476))


d1 = datetime.datetime(2020, 9, 10, 0,0,0)
d2= datetime.datetime(2020, 12, 16, 0,0,0)
print("HPE "+ str(((today-d1).days*53.136143+(today-d2).days*9.7422)/62.878343))

d1 = datetime.datetime(2020, 10, 1, 0,0,0)
d2= datetime.datetime(2020, 12, 16, 0,0,0)
print("HOLX "+ str(((today-d1).days*3.74084+(today-d2).days*3.24977)/6.99061))


d1 = datetime.datetime(2020, 10, 15, 0,0,0)
d2= datetime.datetime(2020, 11, 15, 0,0,0)
d3= datetime.datetime(2021, 1,16, 0,0,0)
print("NIO "+ str(((today-d1).days*10+(today-d2).days*6.079766+(today-d3).days*3)/19.079766))


d1 = datetime.datetime(2020, 12, 1, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
d3= datetime.datetime(2020, 12, 28, 0,0,0)
d4= datetime.datetime(2020, 12, 30, 0,0,0)
d5= datetime.datetime(2020, 12, 31, 0,0,0)
d6= datetime.datetime(2021, 1, 1, 0,0,0)
d7= datetime.datetime(2021, 1, 16, 0,0,0)
d8= datetime.datetime(2021, 1, 19, 0,0,0)
print("BLNK " + str(((today-d1).days*5.217639+(today-d2).days*5.044254+(today-d3).days*5.734492+(today-d4).days*.068087
	+(today-d5).days*.061855+(today-d6).days*4.83922+(today-d7).days*1.696541+(today-d8).days*3.792926)/26.455014))

d1 = datetime.datetime(2020, 10, 9, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
print("ARKQ "+ str(((today-d1).days*10.23+(today-d2).days*1.290297)/10.237481))

d1 = datetime.datetime(2020, 12, 16, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
print("ARKG "+ str(((today-d1).days*5.300346+(today-d2).days*.947456)/6.247802))

d1 = datetime.datetime(2020, 12, 16, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
print("ARKF "+ str(((today-d1).days*10.140763+(today-d2).days*1.031976)/11.172739))

d1 = datetime.datetime(2021, 1, 1, 0,0,0)
d2= datetime.datetime(2021, 1, 19, 0,0,0)
print("ARKK "+ str(((today-d1).days*2.645539+(today-d2).days*3)/5.645539))

d1 = datetime.datetime(2020, 12, 16, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
print("TER "+ str(((today-d1).days*2.097139+(today-d2).days*2.104554)/4.201693))

d1 = datetime.datetime(2020, 11, 1, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
print("C "+ str(((today-d1).days*5+(today-d2).days*1.651118)/6.651118))

d1 = datetime.datetime(2020, 12, 1, 0,0,0)
d2= datetime.datetime(2020, 12, 28, 0,0,0)
print("PLTR "+ str(((today-d1).days*6.005615+(today-d2).days*3.057713)/9.063328))
