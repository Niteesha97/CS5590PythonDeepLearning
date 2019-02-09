class Employee:
    empCount = 0
    tsal = 0
    avgsal = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.tsal += int(salary)

    def average_salary(self):
        print("average salary of %d" % (Employee.tsal / Employee.empCount))

    def explain_interitance(self):
        print("this is from parent class")

    def print_emp(self):
        print("\nname:", self.name, "family:", self.family, "salary:", self.salary, "department:", self.department)


class Fulltime_Employee(Employee):
    def another_method(self):
        print("this is from child class")



emp1 = Employee("bindu", "single ", "1000", "CS")
emp2 = Employee("rishu", "single", "7000", "EE")
emp3 = Employee("navya", "single", "8500", "CS")
emp4 = Employee("tej", "single", "9000", "CS")
emp5 = Fulltime_Employee("harsha", "single", "9000", "CS")
print("Total Employees %d" % Employee.empCount)
print("average salary is %d" % (Employee.tsal / Employee.empCount))

emp2.average_salary()

emp1.print_emp(

)


emp5.explain_interitance()
emp5.another_method()
