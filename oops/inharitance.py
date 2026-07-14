"""class Animal:#parent class
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
class dog(Animal):#child class
    pass

d1=dog()
d1.eat()
d1.sleep()
"""
"""class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):#method overreading
        print("Dog barks")
class Cat(Animal):
    def sound(self): #method overreading
        print("Cat meows")
d1=Dog()
c1=Cat()
d1.sound()
c1.sound()"""

"""class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        super().sound() #calls parent method
        print("Dog barks")
class Cat(Animal):
    def sound(self): #method overreading
        print("Cat meows")
d1=Dog()
c1=Cat()
d1.sound()
c1.sound()
"""
""""class Shape():
    def draw(self):
        print("drawing shape")
class circle(Shape):
    def draw(self):
        print("drawing circle")
class Rectangle(Shape):
    def draw(self):
        print("drawing Rectangle")
#polymorphism
shapes=[circle(),Rectangle()]
for shape in shapes: 
    shape.draw()
"""
"""class Person:
    def show(self):
        print("I am a person")
class Student(Person):
    def show(self):
        super().show()
        print("I am a student")
s1=Student()
s1.show()
"""

#multiinharitance
"""class Camera:
    def photo(self):
        print("Taking photo")
class Musicplayer:
    def music(self):
        print("playing music")
class Smartphone(Camera,Musicplayer):
    pass

p=Smartphone()
p.photo()
p.music()"""

#Multileveliaritance
class GrandFather:
    def hight(self):
        print("tall in hight")
class Father(GrandFather):
    def look(self):
        print("Handsome in look")
class Son(Father):
    def hobby(self):
     print("Hobby is singing")
     

s1=Son()
s1.hight()
s1.look()
s1.hobby()




        