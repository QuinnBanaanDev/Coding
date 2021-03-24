def writeFile(toWrite):
    outFile = open("Ledger.txt", "w") #open file to write
    outFile.write(toWrite)
    outFile.close()

def readFile():
    inFile = open("Ledger.txt", "r") # open file to read
    read = ""
    fileRead = " " # here are the contents of the file 
    for read in inFile:
        fileRead += read
        print(read)
    inFile.close()
    return fileRead

def main():

    userAction = int(input('''
    What do you want to do?
        1. Write to file
        2. Read from file
    '''))

    if userAction == 1:
        
        line1 = "Q"
        msg = ""
        while line1 != "": #handles multiline input
            line1 = input("")
            line2 = input("")
            msg += line1 + "\n" + line2
        writeFile(msg)
    elif userAction == 2:
        readFile()
main()
