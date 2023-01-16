"""
Aggregation : which is provide HAS - Arelationship

inheritnace:  which is provide IS - Arelationship

"""

class salary:
    def __init__(self,currentsalary,bonus):
        self.currentsalary = currentsalary
        self.bonus = bonus

    def annulsalary(self):
        return self.currentsalary*12 + self.bonus

class Employee:
    def __init__(self,name,depart,salary,bonus):
        self.name = name
        self.depart = depart
        self.salary = salary
        self.bonus = bonus

    def tota_sal(self):
        return self.main_salary.annulsalary()

emp = Employee("ddd", "IT", 70000,15000)
print(emp.tota_sal())