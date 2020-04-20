class Point:
    def __init__(self,x,y,z=None):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        if self.z != None:
            print(self.x,self.y,self.z)
        else :
            print(self.x, self.y)

P1=Point(2,3, 5)
P1.ToString()