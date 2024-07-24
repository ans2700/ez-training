'''
oops
class
object
constructor
oops concepts->abstraction,encapsulation,inheritance,polymorphism
props of oops->privacy,multiple objects for single class
>class
class contains->functions,constructor,data
class is a blueprint of objects
class is a logical entity
>object
objects are real world(physical) entity
object is an instance(copy,sub-part) of class
objects contains->properties,behavior,function,identity
>constructor
is a special function which is used to invoke instance(object) variables
constructor returns nothing so don't use constructor
while creating objects constructor will be called implicitly(default)
types of constructor
->default-whenever we run a class without class it uses default constructor
->parameterized
->non-parameterized
self is a self referencing medium, like this pointer
'''
class Student:
    def __init__(self,name,roll,branch,address,email):
        #initializing instance variables
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print('Name:',self.name)
        print('Roll:',self.roll)
        print('branch:',self.branch)
        print('Address:',self.address)
        print('Email:',self.email)
#objects are created outside the class
s1=Student('navya',67,'cse','hyd','n@gmail.com')
#call function to execute
s1.display()
#object.function()
'''
reducing space complexity
static-to allocate memory static and the data is not changed
dynamic-to allocate memory dynamically
should be written outside the class and inside the constructor
'''
class Student:
    #static allocatino
    branch='cse'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def display(self):
        print('Name:',self.name)
        print('Roll:',self.roll)
        #to call,call from the constructor
        print('branch:',Student.branch)
        print('Address:',self.address)
        print('Email:',self.email)
s1=Student('navya',67,'hyd','n@gmail.com')
s1.display()
#memory="8+4+8+8"(for one student)*240=6720 before it was 8640-6720=1920 is saved
'''
static is used to reduce memory
by creating its variable we needn't declare it repeatedly we can diretly take the value
instead of creating a common data create a static data and pass the copy to all the obejcts
'''
#
class Flight:
    fno='22D'
    destination='london'
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def info(self):
        print('Name:',self.name)
        print('Id:',self.id)
        print('Flight number:',Flight.fno)
        print('Destination:',Flight.destination)
f1=Flight('navyasree',10003)
f1.info()
#
class Student:
    #static allocatino
    branch='cse'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    #converting any obeject to string->this returns so use return keyword
    def __str__(self):
        return f'{self.name} {self.roll} {Student.branch} {self.address} {self.email}' 
s1=Student('navya',67,'hyd','n@gmail.com')
#no methods used so removing display function directly print
print(s1)
'''
for output to be in same line we use str function and to print we use f'{}'
if we remove the curly braces then it will print what's there if self.name{self.name} then returns with self name navya
'''
'''
inheritance
single
multiple
multilevel
hierarhial
'''
class JNTU:
    def schedule_academic():
        print('scedule academic')
    def declare_holidays():
        print('national and summer holidays')
    def results():
        print('go to www.jntuh.results.com')
class Sridevi(JNTU):
    def fees():
        print('3rd year fee is 80k')
obj=Sridevi
obj.fees()
obj.schedule_academic()
obj.declare_holidays()
obj.results()
jobj=JNTU
jobj.results()
'''
abstract class
abstraction means hiding implementation and showing functionalities
no body-abstract
body-non abstract
'''
from abc import ABC
#module in package
class RBIBank(ABC):
    def interest():
        pass
    def loan():
        print('loan provided')
class HDFC(RBIBank):
    def interest():
        print('7.5% interest')
class SBI(RBIBank):
    def interest():
        print('11% interest')
class Axis(RBIBank):
    def interest():
        print('9% interested')
aobj=AXIS
aobj.interest()
aobj.loan()
#
import abc
print(dir(abc))
#
from abc import ABC

class Vehicle(ABC):
    def speed():
        pass
    def milege():
        pass
    def model():
        pass
    def breaks():
        print('stop the vehicle')
class RangeRover(Vehicle):
    def speed():
        print('450 max speed')
    def milege():
        print('12KMPH')
    def model():
        print('New model')
class Fortuner(Vehicle):
    def speed():
        print('380 max speed')
    def milege():
        print('15KMPH')
    def model():
        print('Lengender')
fobj=Fortuner
fobj.milege()
fobj.speed()
fobj.model()
fobj.breaks()
        
        
        



