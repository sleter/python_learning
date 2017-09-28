class Time:
    def __init__(self, hour = 0,minute=0,second=0):
        self.hour=hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour,self.minute,self.second)

    def __add__(self, other_time):
        new_time = Time()
        new_time.second += other_time.second + self.second
        if(new_time.second>=60):
            new_time.second-=60
            new_time.minute+=1+other_time.minute + self.minute
        else:
            new_time.minute += other_time.minute + self.minute

        if(new_time.minute>=60):
            new_time.minute-=60
            new_time.hour+=1+other_time.hour + self.hour
        else:
            new_time.hour += other_time.hour + self.hour

        if(new_time.hour>24): new_time.hour-=24

        return new_time

def main():
    time1 = Time(1,20,30)
    print(time1)
    time2 = Time(24,41,30)
    print(time1+time2)


main()
