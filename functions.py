import os
cwd = os.getcwd()
os.chdir(os.getcwd()+'/documentos')
fileList = os.listdir(os.getcwd())
def countOccurrences(busqueda,strpalabras):
    #Implementar un arbol de busqueda binaria para disminuir la complejidad de la funcion.
    count = 0
    listapalabras = strpalabras.split()
    listapalabras.sort()
    for palabra in listapalabras:
        if palabra.lower() == busqueda:
            count+=1
    return count

def createDictionary(word,fileList):
    ubicacionPalabra={}
    estaEnArchivos = 0
    for archivo in fileList:
        lineaXfile = []
        with open(archivo, 'r') as f:
            vecesArchivo = countOccurrences(word,f.read())
            f.seek(0)
            indexLine = 1
            if (vecesArchivo > 0):
                estaEnArchivos = 1
                lines = f.readlines()
                veces=0
                for row in lines:
                    row.strip('\n')
                    if word in row:
                        lineaXfile.append(str(indexLine))
                        veces+=1
                    indexLine+=1
                    ubicacionPalabra[archivo] = lineaXfile
                    if (veces == vecesArchivo):
                        break;
    return (ubicacionPalabra,estaEnArchivos)

def formateo(word,dic):
    print("la palabra %s se encuentra en:" % word.upper())
    for clave, valor in dic.items():
        if len(valor) > 1:
            ultimo = valor[-1]
            valor = valor[:-1]
            ls=", ".join(valor)
            print("   -El documento %s en las lineas: %s y %s" % (clave, ls, ultimo))
        else:
            print("   -El documento %s en la linea: %s" % (clave,valor[0]))

def separateLogicOperators(word):
    list = word.split()
    coincidences = []
    operators = []
    for word in list:
        if word.lower() == 'or':
            operators.append(word)
            list.remove(word)
        if word.lower() == 'and':
            operators.append(word)
            list.remove(word)
    for element in list:
        coincidences.append(createDictionary(element,fileList)[1])
    r = logica(coincidences,operators)
    if r == 1:
        for palabra in list:
            dic, valor = createDictionary(palabra,fileList)
            if(valor == 1):
                formateo(palabra,dic)
    else:
        print("No se encontraron resultados")

def logica(a, b):
    if len(a) > 2:
        if b[0] == "and":
            resultado = a[0] and a[1]
        if b[0] == "or":
            resultado = a[0] or a[1]
        b = b[1:]
        index = 2
        for element in b:
            if element == "and":
                resultado = resultado and a[index]
            if element == "or":
                resultado = resultado or a[index]
            index = index + 1
    elif (len(a) == 2):
        if b[0] == "and":
            resultado = a[0] and a[1]
        if b[0] == "or":
            resultado = a[0] or a[1]
    else:
        resultado = a[0]
    return resultado