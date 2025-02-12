Employee Management System

Objective:

Develop an Employee Management System in Python using object-oriented programming (OOP) principles, adhering to the SOLID design principles. The system categorizes employees into different departments (e.g., Development, Sales, Finance, HR) and handles department-specific responsibilities and salary calculations. Each department has a dedicated manager responsible for overseeing operations, and the system includes flexible logging mechanisms and extensible functionality for future enhancements.

Key Features:

1. Employee Base Class

The Employee class serves as an abstract base class for all employees. It ensures a consistent structure and behavior across all employee types.

Attributes:

name: Name of the employee.

base_salary: The base salary of the employee.

final_salary: The final calculated salary of the employee.

id: Unique identifier for the employee.

Abstract Methods:

calculate_salary(): Must be implemented by derived classes for department-specific salary calculations.

display_info(): Displays employee information, including department-specific details.

2. Department-Specific Employee Classes

Each department has its own class derived from Employee. These classes manage attributes and salary calculations unique to their department:

Developer:

Attributes:

projects: Number of projects handled.

Salary Calculation:

base_salary + (projects * BONUS_PER_PROJECT)

Functionality:

Displays developer-specific details, including project count.

Salesperson:

Attributes:

total_sales: Total sales made.

Salary Calculation:

base_salary + (total_sales * COMMISSION_RATE)

Functionality:

Displays sales-specific details, including total sales.

Accountant:

Attributes:

financial_reports: Number of financial reports handled.

Salary Calculation:

base_salary + (financial_reports * COMMISSION_RATE)

Functionality:

Displays financial-specific details, including reports managed.

HR Representative:

Attributes:

employees_managed: Number of employees directly managed.

Salary Calculation:

base_salary + (employees_managed * BONUS_PER_EMPLOYEE)

Functionality:

Displays HR-specific details, including employees managed.

3. Department Managers

Each department has a dedicated manager responsible for handling the employees in their department.

Responsibilities:

Adding and removing employees.

Displaying details of all employees in the department.

Calculating the total salary of employees in the department.

Ensuring the Single Responsibility Principle (SRP) by focusing on department-specific management.

Implementation:

DeveloperManager, SalesManager, FinanceManager, HRManager classes inherit from a shared base DepartmentManager class.

4. Logging System

To track actions within the system, a flexible logging system is implemented using an ILogger interface:

Logging Implementations:

ConsoleLogger: Logs messages to the console.

FileLogger: Logs messages to a file for persistent records.

Dependency Injection:

The logging mechanism is injected into the system for enhanced flexibility.

5. Centralized Employee Management System

The EmployeeManagementSystem class coordinates operations across all departments.

Functionality:

Add employees to specific departments.

Remove employees by their ID.

Display employees by department.

Calculate total salaries for a specific department.

Supports extensibility for adding new departments or employee types.

Design Principles Followed

Single Responsibility Principle (SRP):

Each class focuses on a specific responsibility. For instance, employee classes focus on individual behavior, while manager classes handle department-level operations.

Open-Closed Principle (OCP):

The system is open for extension (new departments or employee types) but closed for modification (existing functionality remains untouched).

Liskov Substitution Principle (LSP):

All employee classes can be substituted for the base Employee class, ensuring consistent behavior.

Interface Segregation Principle (ISP):

Logging is abstracted into the ILogger interface, allowing multiple logging implementations.

Dependency Inversion Principle (DIP):

Logging and other dependencies are injected into the system, ensuring loose coupling.

Conclusion:

This Employee Management System provides a well-structured, extensible, and maintainable solution for handling employees across multiple departments. By leveraging OOP principles and adhering to the SOLID design principles, it ensures a scalable and efficient architecture for future enhancements.

