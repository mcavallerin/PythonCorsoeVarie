import os, fnmatch
import copy

def searchFileName(path,pattern,fileName):
    listOfFiles = os.listdir(path) 
    f = open(fileName,"w+")
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                #print (entry)
                f.write(entry)
                f.write("\r\n")
    f.close()
    return

def editName(substituteSearchPattern,substituteEditPattern,fileName,newFileName):
    f = open(fileName,"r")
    a = f.readlines()
    f.close()
    f = open(newFileName,"w+")
    for i in a:
            i=i.replace(substituteSearchPattern,substituteEditPattern)
            f.write(i)
    f.close()
    return

def renameFile(path,file1,file2):
    fsrc = open(file1,"r") #source name log file
    fdst = open(file2,"r") #destination name log file
    logFile = open(logEditFileName,"w+")
    logFile.writelines("log dei file rinominati: \n")
    lfsrc = fsrc.read().splitlines()
    lfdst = fdst.read().splitlines()
    for i in range(len(lfsrc)):
            os.rename(path+lfsrc[i],path+lfdst[i])
            logFile.writelines("file rinominato: " + lfsrc[i] + "-->" + lfdst[i] + '\n' )
    fsrc.close()
    fdst.close()
    return

#inizializzazione
path = '/home/michele/Desktop/UntitledFolder/' #percorso dove eseguire l'analisi e la sostituzione
pattern = '* *' #pattern da ricercare
substituteEditPattern = '' #pattern da sostituire '' --> cancella pattern

#variabili d'appoggio
substituteSearchPattern = pattern[1:-1]
fileName = "listaFileIniziale.txt"
newFileName = "nuoviNomiFile.txt"
logEditFileName = "logEditFileName.txt"

#principale
#creo il log di ricerca dei file non corretti
searchFileName(path,pattern,fileName)
#creo il log di rinomina per controllare se è corretto
editName(substituteSearchPattern,substituteEditPattern,fileName,newFileName)

#rinomino i file fisici in path
#renameFile(path,fileName,newFileName)



