import os
def createDictionary():
    palabras = {}
    cwd = os.getcwd()
    os.chdir(os.getcwd()+'\\documentos')
    fileList = os.listdir(os.getcwd())
    for file in fileList:

        with open(file, 'r') as f:

            words = f.read().lower().split()
            for word in words:

                if word[-1] in [',', '!', '?', '.',"'"]:
                    word = word[:-1]
                if word not in palabras.keys():
                    palabras[word] = [f.name]

                else:
                    if file not in palabras[word]:
                        palabras[word] += [f.name]

    return palabras, cwd


def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('indice.txt', 'w') as indexFile:

        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt")] + " ")

            indexFile.write(f'{len(files)}\n')


writeToFile(*createDictionary())