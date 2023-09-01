#  File: Employee.py
#  Student Name:
#  Student UT EID:
#  Partner Name: [DELETE if you did not work with a partner.]
#  Partner UT EID: [DELETE if you did not work with a partner.]


class Employee:

    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    @property
    def salary(self):
        pass
        '''##### ADD CODE HERE #####'''

    @salary.setter
    def salary(self, salary):
        pass
        '''##### ADD CODE HERE #####'''

    @property
    def name(self):
        pass
        '''##### ADD CODE HERE #####'''

    @property
    def id(self):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''

    @property
    def benefits(self):
        pass
        '''##### ADD CODE HERE #####'''

    @benefits.setter
    def benefits(self, benefits):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Manager(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''

    @property
    def bonus(self):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


''' ##### DRIVER CODE #####
    ##### Do not change. '''


def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
