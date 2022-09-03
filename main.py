import os
def createDictionary():
    palabras = {}
    cwd = os.getcwd()
    os.chdir(os.getcwd()+'/documentos')
    fileList = os.listdir(os.getcwd())
    for file in fileList:

        with open(file, 'r') as f:

            lines = f.readlines()
            lineNumber = 1
            for line in lines:
                dic = {}
                words = line.lower().split()
                for word in words:
                    if word[-1] in [',', '!', '?', '.']:
                        word = word[:-1]
                    if word not in palabras.keys():
                        dic[f.name] = [lineNumber]
                        palabras[word] = dic
                    elif file not in palabras[word]:
                        palabras[word][f.name] = [lineNumber]
                    elif lineNumber not in palabras[word][f.name]:
                        palabras[word][f.name] += [lineNumber]

                lineNumber += 1
    return palabras, cwd
createDictionary()