class Fibb:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum


def main():
    #fibb = Fibb()
    #for i in range(10):
    #    print(next(fibb))

    print([i ** 2 for i in range(50) if i % 8 == 0])
    print([x for x in [i * 2 for i in range(10)] if x%8==0])


main()

