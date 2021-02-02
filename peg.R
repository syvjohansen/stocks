library(readxl)
library(ggplot2)
peg <- read_excel("~/stocks/scrapes/peg.xlsx", 
                                 sheet = "Sheet1", col_names = FALSE, na = "NA")

spy <- read_excel("~/stocks/scrapes/spy.xlsx", 
                  sheet = "Sheet1", col_names = FALSE, na = "NA")

port <- read_excel("~/stocks/portfolio/my_portfolio.xlsx", 
                  sheet = "Sheet1", col_names = TRUE, na = "NA")
peg <- data.frame(peg)
colnames(peg) <- c("Stock", "Sector", "Subsector", "Peg")
peg <- na.omit(peg)
peg$Peg <- as.double(sub(",","", peg$Peg, fixed=TRUE))
peg[which(as.double(peg$Peg) < 1 ), ]



peg$Sector[which(peg$Sector=="Communication Services\r\n")] = "Communication Services"
sectors = unique(peg$Sector)
subsectors = unique(peg$Subsector)
mean(as.double((subset(peg, Sector=="Industrials"))$Peg))
secpeg = rep(0, length(sectors))
mediansecpeg = rep(0, length(sectors))
for(a in 1:length(sectors)){
  print(sectors[a])
  secpeg[a] = (mean(as.double((subset(peg, Sector==sectors[a]))$Peg)))
  mediansecpeg[a] = (median(as.double((subset(peg, Sector==sectors[a]))$Peg)))
}
sec_df = cbind(sectors, secpeg, mediansecpeg)


subsecpeg = rep(0, length(subsectors))
for(a in 1:length(subsectors)){
  print(subsectors[a])
  subsecpeg[a] = (mean(as.double((subset(peg, Subsector==subsectors[a]))$Peg)))
}
subsec_df = cbind(subsectors, subsecpeg)

sec_df
HC = peg[which(peg$Sector=="Health Care"), ]
IT = (peg[(which(peg$Sector=="Information Technology")), ])
CS = (peg[(which(peg$Sector =="Communication Services")), ])
FIN = (peg[(which(peg$Sector =="Financials")), ])
NRG = (peg[(which(peg$Sector =="Energy")), ])
CD = (peg[(which(peg$Sector =="Consumer Discretionary")), ])
IND = peg[(which(peg$Sector =="Industrials")), ]
UTL = peg[(which(peg$Sector =="Utilities")), ]
MAT = peg[(which(peg$Sector =="Materials")), ]
RE = peg[(which(peg$Sector =="Real Estate")), ]
STAP = peg[(which(peg$Sector =="Consumer Staples")), ]

summary(IT$Peg)
summary(HC$Peg)
summary(CS$Peg)
summary(FIN$Peg)
summary(CD$Peg)



IT[order(IT$Peg), ]
HC[order(HC$Peg), ]
CS[order(CS$Peg), ]
FIN[order(FIN$Peg), ]
NRG[order(NRG$Peg), ]
CD[order(CD$Peg), ]

peg[order(peg$Peg), ]


ones = peg[which(as.double(peg$Peg) < 1 ), ]
ones[order(ones$Peg), ]

summary(peg$Peg)
q1 = peg[which(as.double(peg$Peg) < summary(peg$Peg)[2] ), ]
q1[order(q1$Peg), ]

spydf <- data.frame(spy)
colnames(spydf) <- c("Date", "Price", "Days")

portdf = data.frame(port)
portdf = portdf[2:length(portdf[,1]), 1:15]
row.names(portdf) = 1:length(portdf[,1])

for(i in 1:length(portdf[,1])){
  if(portdf[i,1] %in% peg$Stock){
    portdf$Peg[i] = peg$Peg[which(peg$Stock==portdf[i,1])]
    print(c(portdf$Asset[i], portdf$Peg[i]))
  }
  else{
    portdf$Peg[i] = NA
  }
}
portdf
portdf2 = portdf

spydf$Date = as.numeric(spydf$Date)
portdf$Day.Bought = as.numeric(portdf$Day.Bought)


min(spydf$Date)
portdf <- portdf[-c(which(portdf$Day.Bought < min(spydf$Date))), ]
row.names(portdf) = 1:length(portdf[,1])



portdf[2,9]
which(spydf$Date==portdf[2,9])

#spydf$Days = max(spydf$Days) - spydf$Days
lm(spydf$Price~spydf$Days)

adbespy <- spydf[1:39, ]
adbespy$Days <- max(adbespy$Days) - adbespy$Days
adbespy$pc = (adbespy$Price-adbespy$Price[length(adbespy$Price)])/adbespy$Price[length(adbespy$Price)]
adbespy$def = adbespy$Price/adbespy$Price[length(adbespy$Price)]
adbespy$apy = adbespy$pc/(adbespy$Days/365)*100
#adbespy$apy[length(adbespy$apy)] = 0
#summary(glm(apy~Days, data=adbespy))
#summary(lm(adbespy$def~adbespy$Days))


#adbespy = sapply(adbespy, sd)
adbe.lm = (glm(def~Days, data=adbespy))
adbe.stand = portdf[2,4]/portdf[2,3]
adbe.stand=(adbe.stand-portdf[2,3]/portdf[2,3])/portdf[2,10]
se = summary(adbe.lm)[12][[1]][2,2]
adbe.lm$coefficients[2]
se
adbescore = 
se(adbe.lm)
confint(adbe.lm)

#confint(adbe.lm)
#confint(adbe.lm)[2,2] > portdf[2,4]/portdf[2,3]/portdf[2,10]
#summary(adbe.lm)


vtick = c()
vapy = c()
vspct = c()
verror = c()
vprob = c()
vpeg = c()

for(a in 2:length(portdf[,1])){
  sspy <- which(spydf$Date==portdf[a,9])
  #print(sspy)
 # print(sspy)
  if(length(sspy)<1){
    next
  }
  else if(sspy<=1){
    next
  }
  else{
    sspy = spydf[1:sspy, ]
    sspy$Days <- max(sspy$Days) - sspy$Days
    sspy$pc = (sspy$Price-sspy$Price[length(sspy$Price)])/sspy$Price[length(sspy$Price)]
    sspy$def = sspy$Price/sspy$Price[length(sspy$Price)]
    
    
    #summary(lm(sspy$def~sspy$Days))
    
    
    #sspy = sapply(sspy, sd)
    s.lm = (glm(def~Days, data=sspy))
    #confint(s.lm)
   # print(portdf[a,1])
    #portdf[a,4]
    port.stand = portdf[a,4]/portdf[a,3]
    cf = confint(s.lm)[2,2] > (port.stand-portdf[a,3]/portdf[a,3])/portdf[a,10]
    port.stand=(port.stand-portdf[a,3]/portdf[a,3])/portdf[a,10]
    se = summary(s.lm)[12][[1]][2,2]
    #print(cf)
    chance = 1-pnorm(((port.stand-s.lm$coefficients[2])/se)[[1]])
    # vspy[a,] = c(as.character(portdf[a,1])
    #              , as.double(portdf[a,7]),
    #              as.double(sspy$pc[1]*100)
    #              , as.double(((port.stand-s.lm$coefficients[2])/se)[[1]]), 
    #              as.double(chance) )
    # vspy$ticker[a] = (portdf[a,1])
    # vspy$apy[a] = portdf[a,7]
    # vspy$spct[a] = sspy$pc[1]*100
    # vspy$error[a] = ((port.stand-s.lm$coefficients[2])/se)[[1]]
    # vspy$prob[a] = chance
   #  print(portdf[a,1])
   # print(c(portdf[a,7],  sspy$pc[1]*100))
   # print(((port.stand-s.lm$coefficients[2])/se)[[1]])
   # print(chance)
   vtick = append(vtick, portdf[a,1])
   vapy = append(vapy, portdf[a,7])
   vspct = append(vspct,sspy$pc[1]*100 )
   verror = append(verror,((port.stand-s.lm$coefficients[2])/se)[[1]] )
   vprob = append(vprob, chance)
   vpeg = append(vpeg, portdf[a,15])
    #print(cf)
  }
}
vspy = data.frame(vtick, vapy, vspct, verror, vprob, vpeg)
# for(i in 1:length(vspy[,1])){
#   if(vspy[i,1] %in% peg$Stock){
#     vspy$Peg[i] = peg$Peg[which(peg$Stock==vspy[i,1])]
#     #print(c(vspy$Asset[i], portdf$Peg[i]))
#   }
#   else{
#     vspy$Peg[i] = NA
#   }
# }

colnames(vspy) = c("Ticker", "Pct", "SPY Pct", "Zscore", "Prob", "Peg")

print(vspy[order(vspy$Zscore), ])

ggplot(vspy, aes(x=Peg, y=Zscore))+geom_point()
cor(vspy$Peg, vspy$Zscore, use="complete.obs")
summary(glm(Zscore~Peg, data=vspy))




