def get_x():
    return 'get_x'

class MyClass:
    def __init__(self):
        self.x = 0

    def get_x(self):
        return self.x

    def incr(self):
        self.x += 1
        return self.get_x()

    def decr(self):
        self.x -=1
        return get_x() #self가 안붙어서 외부의 다른 함수가 불려진다

a = MyClass()

print(a.incr())
print(a.decr())

class window:
    def __init__(self):
        self.x =100
        self.y = 100
        self.width = 640
        self.height = 480


    def set_width(self,w):
        if( isinstance(w,int)):
            if(w<= 639):
                print('you input invalid number')
            else:
                self.width = w
                print(self.width)



b = window()

b.set_width(650)

