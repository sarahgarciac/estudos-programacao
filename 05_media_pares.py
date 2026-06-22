#Escreva um algoritmo que calcula a media dos numeros pares de 1 ate 100 - 1 e 100 inclusos - usando o for
numeros_pares = [] #podia ter feito variavel soma = 0 
quantidade = 0 

for i in range(1,101):
    if i % 2 == 0:
        numeros_pares.append(i) #poderia ter feito soma += 1
        quantidade = quantidade + 1 # poderia ter escrito quantidade += 1

total = sum(numeros_pares)

media = total / quantidade 

print(f"A média dos números pares entre 1 e 100 é: {media} ")
