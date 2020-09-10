library(readxl)
peg <- read_excel("~/stocks/scrapes/peg.xlsx", 
                                 sheet = "Sheet1", col_names = FALSE, na = "NA")

peg <- data.frame(peg)
colnames(peg) <- c("Stock", "Sector", "Subsector", "Peg")
peg <- na.omit(peg)
peg[which(as.double(peg$Peg) < 1 ), ]

sectors = unique(peg$Sector)
subsectors = unique(peg$Subsector)

which(peg$Sector=="Communication Services\r\n")

mean(as.double((subset(peg, Sector=="Industrials"))$Peg))
secpeg = rep(0, length(sectors))
for(a in 1:length(sectors)){
  print(sectors[a])
  secpeg[a] = (mean(as.double((subset(peg, Sector==sectors[a]))$Peg)))
}
sec_df = cbind(sectors, secpeg)


subsecpeg = rep(0, length(subsectors))
for(a in 1:length(subsectors)){
  print(subsectors[a])
  subsecpeg[a] = (mean(as.double((subset(peg, Subsector==subsectors[a]))$Peg)))
}
subsec_df = cbind(subsectors, subsecpeg)

peg[which(peg$Sector=="Health Care"), ]

