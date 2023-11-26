Class vecteur2D:
    count = 0

    def _init_(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        Vecteur2D.count +=1

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def Tostring(self):
        return f"X = {self.x}; Y = {self.y}"
    
    def equals(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False
    
    def norme(self):
        return (self.x *2 + self.y **2) * 0.5
    

class vecteur3D(Vecteur2D):

    def _init_(self, x = 0.0 , y = 0.0 , z = 0.0):
            super()._init_(x, y)
            self.z = z

    def Tostring(self):
            return f"X = {self.x}; Y = {self.y} ; Z = {self.z}"
        
    def equals(self,point):
            if self.x == point.x and self.y == point.y and self.z == point:
                return True
            else:
                return False
            
    def norme(self):
        return (self.x *2 + self.y **2 + self.z **2) * 0.5

v1 = Vecteur2D(1.9, 3)
v2 = Vecteur2D(1.9, 3)
v3 = vecteur3D(1.9 , 2 , 7)


print(f"Number of objects: {Vecteur2D.count}")

print("v1:", v1.Tostring())
print("v2:", v2.Tostring())
print("v3:", v3.Tostring())

print("v1 equals v2:", v1.equals(v2))
print("v1 equals v3:", v1.equals(v3))

print("Norme of v1:", v1.norme())
print("Norme of v3:", v3.norme())
