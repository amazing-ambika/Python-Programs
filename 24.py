# class named as circle by a radius and two methods of computer area and perimeter of a circle.

#using math package
import math
# #using math functions
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
#read value of area input from user
rad=int(input("Enter radius of circle: "))
#Object for Class
obj=circle(rad)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))
