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
print("AMD "+ str(((today-d1).days*12+(today-d2).days*5+(today-d3).days*5+(today-d4).days*10
	+(today-d5).days*10+(today-d6).days*7+(today-d7).days*1.081549+(today-d8).days*.036672)/50.118221))


d1 = datetime.datetime(2016, 2, 12, 0,0,0)
d2= datetime.datetime(2016, 2, 23, 0,0,0)
d3= datetime.datetime(2017, 5, 5, 0,0,0)
d4= datetime.datetime(2020, 8, 11, 0,0,0)
d5= datetime.datetime(2020, 8, 24, 0,0,0)
d6= datetime.datetime(2020, 8, 25, 0,0,0)
d7= datetime.datetime(2020, 9, 1, 0,0,0)
d8=datetime.datetime(2020, 9, 16, 0,0,0)
print("BABA "+ str(((today-d1).days*1+(today-d2).days*1+(today-d3).days*5+(today-d4).days*4
	+(today-d5).days*1.694136+(today-d6).days*.260491+(today-d7).days*.344934+(today-d8).days*.060534)/13.360095))

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
print("LIT "+ str(((today-d1).days*13.384771+(today-d2).days*.051391+(today-d3).days*.371732)/13.807894))


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
print("NVDA "+ str(((today-d1).days*2+(today-d2).days*5+(today-d3).days*5)/12))

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








