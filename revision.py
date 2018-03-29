def selection_sort(list):
    for i, e in enumerate(list):
        min_ = min(range(i,len(list)), key=list.__getitem__)
        list[i], list[min_] = list[min_], e
    return list 

def fib(x):
    if(x == 0): return 1
    elif(x == 1): return 1
    else:
        return fib(x-1)+fib(x-2)

def palindrom(x):
    if(str(x) == str(x)[::-1]):
        return True
    else: return False

import math
def isPrime(n):
    if n % 2 == 0 and n > 2: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def reszta(x):
    nominaly = [1,2,5,10,20,50,100,200]
    tab = []
    while(x>0):
        for nom in reversed(nominaly):
            if(nom<=x):
                x -= nom
                tab.append(nom)
    return tab

def pasc_triangle(x):
    line = [1]
    print(line)
    for i in range(x-1):
        liny = [1]
        for j in range(len(line)-1):
            liny.append(line[j]+line[j+1])
        liny.append(1)
        line = liny
        print(line)

def get_rows(tab, x):
    pom = []
    pom_exit = []
    for i in range(x):
        pom.append(tab[i])
    pom_exit.append(pom)
    pom=[]
    for i in range(x,len(tab)):
        pom.append(tab[i])
    pom_exit.append(pom)
    return pom_exit

def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


print(fib(7))
print(palindrom("olo"))
print(palindrom("ola"))
print(isPrime(3))
print(isPrime(24))
print(str(reszta(13))+' '+str(len(reszta(13)))+' '+str(reszta(76)))
pasc_triangle(10)
print(get_rows([1, 2, 3, 4, 5], 3))


class Person(object):
    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(self.name)

class SuperHero(Person):
    def __init__(self, name, heroName):
        super(SuperHero, self).__init__(name)
        self.heroName = heroName

    def showInfo(self):
        super(SuperHero, self).showInfo()
        print(self.heroName)


p1 = Person('Jacek')
p1.showInfo()

p2 = SuperHero('Tom','Destroyer')
p2.showInfo()
