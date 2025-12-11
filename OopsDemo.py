#classes are user defined blueprint or prototype from which objects are created
#sum,multiply,divide,substract,constant
#methods,class variables,insatnace variables,constructor
#object for your classes




# self keyword is mandatory for calling variables name into methods
#insatnace and class variables have whole different purpose
#constructor name should  be __init__  it is a special method
#new keyword is not used in python to create object
class Calculator:
    num =100   #class variables
     # default constructor
    def __init__(self, a,b):   #instance variables
           self.frist=a
           self.second=b
           print("I am constructor")
    def  getData(self):
        print("I am now execution as methos in class")

    def Sum(self):
        return self.frist + self.second + Calculator.num


obj=Calculator(2,3)    #syntax to create object in python
obj.getData()
print(obj.Sum())
 
 
obj1=Calculator(4,5)    #syntax to create object in python
obj1.getData()
print(obj1.Sum())
 

        