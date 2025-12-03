
# Media com funcoes std do R
media_1 <- function(v){
  tamanho <- length(v)
  soma <- sum(v)
  return( soma / tamanho )
}

media_2 <- function(v){
  soma <- 0
  for (e in v) {
    soma <- soma + e
  }
  return( soma / length(v))
}

lista_1 <- c(9, 8, 7, 6, 5, 4)
lista_2 <- c(100, 5, 20, 75, 30)
lista_3 <- c(15, 27)

"primeira funcao"
media_1(lista_1)
media_1(lista_2)
media_1(lista_3)
"segunda funcao"
media_2(lista_1)
media_2(lista_2)
media_2(lista_3)

