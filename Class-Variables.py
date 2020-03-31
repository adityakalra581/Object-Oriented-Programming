## Class Variables: Defined in a class, outside the Method. These Variables are also known as static variables as they 
# are same for every instance. 


class Student:

    ## Class Variables:
    num_of_stu = 0
    fee_per_course = 1000
    ## These two only.
    def __init__(self,name,marks,rollno,course):
        ## These all down here are Instance Variables:
        self.name = name
        self.marks = marks
        self.rollno = rollno
        self.course = course
        self.adm_id = name+rollno+"XYZ"
## Specific for Instances. Instances are also known as Objects.
## Instance Variables will vary for different Instances.

        Student.num_of_stu +=1 
        ## number of Students: will be equal to total number of Instances.

## Task: Calculating Fees of a Student:
    ## Ans: We have to create a method for this as this is a new value.
    
    def total_fees(self):
        return '{}'.format(self.course * Student.fee_per_course)

## only 1 Curly brackets is needed


## Let's create some Instances:

stu_1 = Student("Ajay",23,"9",3)
stu_2 = Student("Aman",13,"17",2)
stu_3 = Student("Akash",26,"2",4)


## Instance Variable
print("Admision Id of Student 1:",stu_1.adm_id)

print("Roll number of Student 2:",stu_2.rollno)

print("Name of Student 3:",stu_3.name)

# Class(static Variable)
print("Total number of Students:",Student.num_of_stu)
print("Total Fees of Student 1:",stu_1.total_fees())
print("Total Fees of Student 2:",stu_2.total_fees())
print("Total Fees of Student 3:",stu_3.total_fees())


################################
## OUTPUT:


# Admision Id of Student 1: Ajay9XYZ
# Roll number of Student 2: 17
# Name of Student 3: Akash
# Total number of Students: 3
# Total Fees of Student 1: 3000
# Total Fees of Student 2: 2000
# Total Fees of Student 3: 4000

############################################