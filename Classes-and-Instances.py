class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '' + last + '@company.com'
        ## Notice: that email is not given as parameter, as it is built using already provided parameters.


    ## Let's create a method that will give us the fullname of an employee.
    ## Every method should have self constructor as a parameter in it.
    ## As whenever the method is called by an object, that object will be passed as an argument in it.
    def fullname(self):   
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee("Aman","Singh",25000)

print("The Firstname of the Employee 1 is: ",emp_1.first)
print("The Lastname of the Employee 1 is: ",emp_1.last)

## Print fullname using fullname method
## Remember to use parenthesis for calling a method unlike other parameters.
print("The Fullname of the Employee 1 is: ",emp_1.fullname())


# OUTPUT:
# PS D:\GITHUB\Object-Oriented-Programming> & C:/Python/Python38/python.exe d:/GITHUB/Object-Oriented-Programming/Classes-and-Instances.py        
# The Firstname of the Employee 1 is:  Aman
# The Lastname of the Employee 1 is:  Singh
# The Fullname of the Employee 1 is:  Aman Singh


print()
## Let's create another Object:

emp_2 = Employee("Ujjwal","Jain",30000)

print("The Pay of the Employee 2 is: ",emp_2.pay)
print("The Email of the Employee 2 is: ",emp_2.email)

## Print fullname using fullname method
## Remember to use parenthesis for calling a method unlike other parameters.
print("The Fullname of the Employee 2 is: ",emp_2.fullname())


# OUTPUT of this Code:

# The Pay of the Employee 2 is:  30000
# The Email of the Employee 2 is:  UjjwalJain@company.com
# The Fullname of the Employee 2 is:  Ujjwal Jain

