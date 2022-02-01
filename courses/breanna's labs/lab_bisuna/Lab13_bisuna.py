"""
Lab 13 - Define an employee class with name, hours worked, hourly rate
Programmed by: Breanna Bisuna
Date: 24Nov2020
"""


class Employee:
    """ Employee Definition """
    def __init__(self, name="", hours=0, rate=0):
        """ Define an Employee class with 3 instance variables name, hours, rate """
        self.name = name
        self.hours = hours
        self.rate = rate

    def set_name(self, name):
        """ defining a setter for the name instance variable """
        self.name = name

    def set_hours(self, hours):
        """ define a setter for the hours instance variable """
        self.hours = hours

    def set_rate(self, rate):
        """ define a setter for the hours instance variable """
        self.rate = rate

    def get_name(self):
        """ defining a getter for the name instance variable """
        return self.name

    def get_hours(self):
        """ defining a getter for the hours instance variable """
        return self.hours

    def get_rate(self):
        """ defining a getter for the rate instance variable """
        return self.rate

def main():
    """ driver """
    # Construct an Employee object
    my_employee = Employee()  # Default parameters
    my_employee1 = Employee("Breanna", 15, 10)  # With parameters

    # Use getters to display the processor and ram for the computer
    # you constructed
    print("The Employee name is", my_employee.get_name(), "with",
          my_employee.get_hours(), "hours worked at a rate of",
          my_employee.get_rate(), "per hour.")
    print("The Employee name is", my_employee1.get_name(), "with",
          my_employee1.get_hours(), "hours worked at a rate of",
          my_employee1.get_rate(), "per hour.")

if __name__ == '__main__':
    main()
