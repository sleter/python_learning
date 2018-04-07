from pprint import pprint

x=2
y=9
print(hex(id(x)))
y=x
print(hex(id(y)))

list_ = [1,2,3]
list_.append([1,2,3])
print(list_)
try:
    del list_[10]
except IndexError:
    print('gotcha')

print(list_*2)
list_ += [3]
print(list_)
list_ *= 3
print(list_)

pom = [1,1,3,4,5,3]
print(pom)
print(set(pom))

my_list = [1,2,3.0,'python']
my_list.append([1,2])
print(my_list[2])
my_list[2] = 4.04
print(my_list)

print([2,4] in [2,4,6,7])
print([2,4] in [[2,4],[6,7]])
print('Python' in ['Python costam','cokolwiek'])

for i in range(300,0,-50):
    print(i)
print('------------')
for i in range(0,100,-1):
    print(i)
#nic się nie dzieje
print('------------')

matrix_comprehensions = [(x,y) for x in range(1,4) for y in range(1,4)]
print(matrix_comprehensions)

multiplication_table = {x: {y:y*x for y in range(1,11)} for x in range (1,11)}
pprint(multiplication_table)

print('-----decorators-----')

def my_decorator(func):
    def fun_wrapper(x):
        x+=2
        func(x)
    return fun_wrapper

@my_decorator
def print_x(x):
    print(x)

print_x(2)


def html_p_decorator(func):
    def fun_wrapper(x):
        func('<p>'+x+'</p>')
    return fun_wrapper

@html_p_decorator
def put_text_on_site(my_text):
    print(my_text)

put_text_on_site('lorem ipsum lalalal...')


class A:
    """Klasa A"""
    class Meta:
        a='cos'
    def __init__(self):
        print('__init__@A')
    def hello(self):
        """Metoda hello"""
        pass

ob = A()
dir(ob)
print(ob.__doc__)
print(ob.hello.__doc__)
dir(ob.hello())
print(A.Meta)

class BaseCar:
    def __init__(self, engine=False):
        self._engine=engine

    def startEngine(self):
        self._engine=True

    def return_engine(self):
        return self._engine

class GasCar(BaseCar):
    def __init__(self):
        super().__init__()

    def drive(self):
        print('bruuum')

class DieselCar(BaseCar):
    def __init__(self):
        super().__init__()

    def drive(self):
        if(not BaseCar.return_engine):
            print('First of all start the engine')
        else:
            print('pyr pyr pyr')




car = GasCar()
car2 = DieselCar()

car.drive()
car2.drive()
car2.startEngine()
car2.drive()

#python debbugger
#import pdb; pdb.set_trace()

import string


vowel = ['a', 'o', 'e', 'q', 'u']
output = []
print('Podaj znaki: ')
input = input('>')
for i in input:
    if(i in vowel):
        output.append(i)
    else:
        continue
print(set(output))


