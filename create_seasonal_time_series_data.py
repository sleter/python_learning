from matplotlib import pyplot as plt
from numpy import arange, sin, pi
import numpy as np


class CreateData:
    def __init__(self, function=sin(pi*np.arange(0.0, 2.0, 0.01)), start=0.0, stop=2.0, step=0.01, bottom_h=-2, top_h=2):
        self.bottom_h = bottom_h
        self.top_h = top_h
        self.function = function
        #plot data
        self.t = np.arange(start, stop, step)
        self.fig = plt.figure()
        #output arrays
        self.basic_array = []
        self.noise_array = []
        self.multiplied_array = []
        self.const_value_array = []
        #subplot count (4 max subplots in one column)
        self.sub_c = 410

    def create_subplot(self, function):
        self.sub_c += 1
        ax = self.fig.add_subplot(self.sub_c)
        ax.plot(self.t, function)
        ax.grid(True)
        ax.set_ylim((self.bottom_h,self.top_h))

    def create(self, x, y):
        #example
        
        self.basic_array = self.function

        self.create_subplot(self.function)

        self.create_subplot(self.noise(self.function, 0.3, x, y))

        self.create_subplot(self.multiply(self.function, 0.4, x, y))

        self.create_subplot(self.const(self.function, 1, x, y))

        plt.tight_layout()
        plt.show()

    def return_array(self, type=''):
        if type == 'multiply':
            print(self.multiplied_array)
            return self.multiplied_array
        elif type == 'const':
            print(self.const_value_array)
            return self.const_value_array
        elif type == 'noise':
            print(self.noise_array)
            return self.noise_array
        else:
            print "ReturnArrayError: Not valid argument\nInsert type: multiply, const, noise"

    def noise(self, function, scale, x, y): 
        fun = np.copy(function)
        fun[x:y] = np.random.normal(0, scale, fun[x:y].shape)
        fun += function
        self.noise_array = fun
        return fun

    def multiply(self, function, const, x, y):
        for i in range(x, y):
            function[i] *= const
        self.multiplied_array = function
        return function 

    def const(self, function, const, x, y):
        function[x:y] = const
        self.const_value_array = function
        return function

if __name__ == "__main__":
    #possibilty to override default values
    """ there is dafault sine function, but with proper parameters you can 
    create your own more complicated repetative fuction or just enter numpy array """
    data = CreateData()
    #range(x=30, y=100)
    data.create(30, 100)
    data.return_array(type='noise')