myFile1 = open("mydata2.txt", "w")
myFile1.write("abc")
myFile1.close()

def openFile(name):
    text = open(name).read()
    print("File {}: ".format(name),text)

try:
    openFile("mydata2.txt")
    openFile("mydata3.txt")


except FileNotFoundError as ex:
    print("File not found error!")
    print(ex.args)
finally:
    print("Finished working with file")
