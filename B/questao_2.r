install.packages("patchwork")
library(patchwork)
install.packages("ggplot2")
library(ggplot2)

dados <- read.csv("./questao_2.csv")

p1 <-ggplot(dados, aes(x=Estado_civil)) + geom_bar()
p2 <- ggplot(dados, aes(x=Regiao_de_procedencia)) + geom_bar()
p3 <- ggplot(dados, aes(x=N_de_filhos)) + geom_bar()
p4 <- ggplot(dados, aes(x=idade)) + geom_bar()

(p1 | p2) / (p3 | p4)


