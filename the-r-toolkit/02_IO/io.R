setwd('C:/Users/manising/Documents/housesalesprediction')

ds<-read.csv(file='kc_house_data.csv', header=TRUE)

library(xlsx)

ds1<-read.xlsx(file='au_data.xlsx', sheetIndex = 1,startRow=15,header=FALSE)


save(ds1, file='AUData.RData')
