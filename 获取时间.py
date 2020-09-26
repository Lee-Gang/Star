import time
class Clock(object):
    __slots__ = ("hours","minutes","seconds")
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours= hours
        self.minutes=minutes
        self.seconds=seconds

    def run(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                if self.hours == 24:
                    self.hours=0



    def show(self):
        print("\r%.2d:%.2d:%.2d" % (self.hours, self.minutes, self.seconds),end="")


if __name__ == '__main__':

    t = time.localtime()
    c = Clock(hours=t[3],minutes=t[4],seconds=t[5])
    while True:
        c.show()
        c.run()
        time.sleep(1)
        c.show()
