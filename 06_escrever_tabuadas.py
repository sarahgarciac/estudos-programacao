#Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10. 


for tabuada in range(1,11): 
    print(f"TABUADA DO {tabuada}")
    for i in range(1,11): 
        print(f"{tabuada} X {i} = {tabuada * i}") 
