# Imports
library(ggplot2)
library(reshape)

# Report Twitter Scatter Plot 
resulting_data <- read.csv("~/visualization_data.csv")

resulting_data$
# Ggplot
ggplot(resulting_data, aes(x=Net.Score, y = Number.of.Retweets,  col = ifelse(Net.Score < 0,'blue','red'))) + 
  geom_point() +
  geom_vline(xintercept = 0, linetype = "dotted")  + labs(title = "Num. Retweets Vs. Net Score Scatter Plot ", color='Net Score Value')+ 
  scale_x_discrete(limit = c(-3,-2,-1,0,1,2,3)) + 
  scale_y_discrete(limit = c(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85)) + 
  theme(legend.position = "none")

plot(resulting_data$Net.Score, resulting_data$Number.of.Retweets)
