lista_vazia = []
fname = input("Enter file name: ")
fh = open(fname)

for x in fh:
    transformar_string = str(fh)
    tirar = x.rstrip()
    transformar_lista = tirar.split()

[lista_vazia.append(x) for x in fh if x not in lista_vazia]

lista_vazia.sort()
    
print(lista_vazia)
