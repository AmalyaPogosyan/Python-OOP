from abc import ABC, abstractmethod

# Logger Interface
class ILogger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(ILogger):
    def log(self, message: str):
        print(f"[LOG]: {message}")

class FileLogger(ILogger):
    def __init__(self, filename="log.txt"):
        self.filename = filename
    
    def log(self, message: str):
        with open(self.filename, "a") as file:
            file.write(f"[LOG]: {message}\n")

# Base Employee Class
class Employee(ABC):
    _id_counter = 1000  # Unique ID Counter

    def __init__(self, name, base_salary=75000):
        self.id = Employee._id_counter
        self.name = name
        self.base_salary = base_salary
        self.final_salary = self.calculate_salary()
        Employee._id_counter += 1
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def display_info(self):
        print(f"Name: {self.name} | ID: {self.id} | Final Salary: {self.final_salary}")

# Department-Specific Employees
class Developer(Employee):
    BONUS_PER_PROJECT = 20000
    
    def __init__(self, name, projects=0):
        self.projects = projects
        super().__init__(name)
        self.final_salary = self.calculate_salary()
    
    def calculate_salary(self):
        return self.base_salary + (self.projects * self.BONUS_PER_PROJECT)

class SalesPerson(Employee):
    COMMISSION_RATE = 10000
    
    def __init__(self, name, total_sales=0):
        self.total_sales = total_sales
        super().__init__(name)
        self.final_salary = self.calculate_salary()
    
    def calculate_salary(self):
        return self.base_salary + (self.total_sales * self.COMMISSION_RATE)

class Accountant(Employee):
    COMMISSION_RATE = 5000
    
    def __init__(self, name, reports=0):
        self.reports = reports
        super().__init__(name)
        self.final_salary = self.calculate_salary()
    
    def calculate_salary(self):
        return self.base_salary + (self.reports * self.COMMISSION_RATE)

class HRRepresentative(Employee):
    BONUS_PER_EMPLOYEE = 5000
    
    def __init__(self, name, employees_managed=0):
        self.employees_managed = employees_managed
        super().__init__(name)
        self.final_salary = self.calculate_salary()
    
    def calculate_salary(self):
        return self.base_salary + (self.employees_managed * self.BONUS_PER_EMPLOYEE)

# Department Manager
class DepartmentManager:
    def __init__(self, department_name, logger: ILogger):
        self.department_name = department_name
        self.employees = set()
        self.logger = logger
    
    def add_employee(self, employee: Employee):
        self.employees.add(employee)
        self.logger.log(f"Added {employee.name} to {self.department_name} Department.")
    
    def remove_employee(self, employee: Employee):
        if employee in self.employees:
            self.employees.remove(employee)
            self.logger.log(f"Removed {employee.name} from {self.department_name} Department.")
        else:
            self.logger.log(f"ERROR: {employee.name} not found in {self.department_name} Department.")
    
    def display_employees(self):
        print(f"\n{self.department_name} Department Employees:")
        for employee in self.employees:
            employee.display_info()
    
    def total_salary(self):
        return sum(emp.final_salary for emp in self.employees)

# Employee Management System
class EmployeeManagementSystem:
    def __init__(self, logger: ILogger):
        self.departments = {}
        self.logger = logger
    
    def add_department(self, department_name):
        self.departments[department_name] = DepartmentManager(department_name, self.logger)
    
    def add_employee(self, department_name, employee):
        if department_name in self.departments:
            self.departments[department_name].add_employee(employee)
        else:
            self.logger.log(f"ERROR: Department {department_name} does not exist!")
    
    def remove_employee(self, department_name, employee):
        if department_name in self.departments:
            self.departments[department_name].remove_employee(employee)
        else:
            self.logger.log(f"ERROR: Department {department_name} does not exist!")
    
    def display_department_employees(self, department_name):
        if department_name in self.departments:
            self.departments[department_name].display_employees()
        else:
            self.logger.log(f"ERROR: Department {department_name} does not exist!")
    
    def total_department_salary(self, department_name):
        if department_name in self.departments:
            total_salary = self.departments[department_name].total_salary()
            print(f"Total Salary for {department_name}: {total_salary}")
        else:
            self.logger.log(f"ERROR: Department {department_name} does not exist!")

# Main Function
def main():
    logger = ConsoleLogger()
    ems = EmployeeManagementSystem(logger)
    
    # Adding Departments
    for dept in ["Developer", "Sales", "Finance", "HR"]:
        ems.add_department(dept)
    
    # Adding Employees
    dev1 = Developer("Aram", 2)
    sales1 = SalesPerson("Raymond", 5)
    hr1 = HRRepresentative("Garnik", 10)
    acc1 = Accountant("Laris", 7)
    
    ems.add_employee("Developer", dev1)
    ems.add_employee("Sales", sales1)
    ems.add_employee("HR", hr1)
    ems.add_employee("Finance", acc1)
    
    # Display Employees
    ems.display_department_employees("Developer")
    ems.display_department_employees("Sales")
    
    # Remove an Employee
    ems.remove_employee("Developer", dev1)
    ems.display_department_employees("Developer")
    
    # Calculate Total Salary
    ems.total_department_salary("Sales")

if __name__ == "__main__":
    main()

