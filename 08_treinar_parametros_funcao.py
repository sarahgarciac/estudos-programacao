#escreva uma rotina que crie uma borda ao redor de uma palavra, para destacá-lo como sendo um título. A rotina deve receber como parâmetro a palavra a ser destacada. O tamanho da caixa de texto deve ser adaptável, de acordo com o tamanho da palavra

def borda(x):
    print(f"+{"-" * int(len(x))}+")
    print(f"|{x}|") #poderia colocar separados por vírgualas sem as chaves, mas isso colocaria um espaço aut.
    print(f"+{"-" * int(len(x))}+")

x = input("Insira uma palavra:")

borda(x)
