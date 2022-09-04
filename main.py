import functions as fn
continuar = True
while(continuar):
    word = str(input("word="))
    if(word ==''):
        continuar=False
        print("Gracias por usar el indice de palabras")
    else:
        fn.separateLogicOperators(word)
