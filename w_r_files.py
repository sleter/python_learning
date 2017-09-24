import os

def fib(num):
    if num==0 : return 1
    elif num==1 : return 1
    else: return fib(num-1)+fib(num-2)

def store_fib(n):
    with open("mydata.txt",mode = "w",encoding ="utf-8") as myFile:
        #print(os.getcwd())
        for i in range(0,n):
            myFile.write(str(fib(i))+"\n")


def read_file():
    with open("mydata.txt",encoding = "utf-8") as myFile :
        line_num = 1
        while True :
            line = myFile.readline()
            if not line : break
            print("Line {} : Text {}".format(str(line_num),line),end="")
            line_num+=1



def main():
    how_many = int(input("Enter : "))
    store_fib(how_many)
    read_file()

main()
