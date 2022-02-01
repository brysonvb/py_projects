"""
Lab 13 - Define an employee class with name, hours worked, hourly rate
Programmed by: Breanna Bisuna
Date: 24Nov2020
"""


class Employee:
    def __init__(self, name="", hours=0, rate=0):
        # Define an Employee class with 3 instance variables name, hours, rate
        self.name = name
        self.hours = hours
        self.rate = rate

    # defining a setter for the name instance variable
    def set_name(self, name):
        self.name = name

    # define a setter for the hours instance variable
    def set_hours(self, hours):
        self.hours = hours

    # define a setter for the hours instance variable
    def set_rate(self, rate):
        self.rate = rate

    # defining a getter for the name instance variable
    def get_name(self):
        return self.name

    # defining a getter for the hours instance variable
    def get_hours(self):
        return self.hours

    # defining a getter for the rate instance variable
    def get_rate(self):
        return self.rate


def main():
    # Construct an Employee object
    myEmployee = Employee()  # Default parameters
    myEmployee1 = Employee("Breanna", 15, 10)  # With parameters

    # Use getters to display the processor and ram for the computer
    # you constructed
    print("The Employee name is", myEmployee.get_name(), "with",
          myEmployee.get_hours(), "hours worked at a rate of",
          myEmployee.get_rate(), "per hour.")
    print("The Employee name is", myEmployee1.get_name(), "with",
          myEmployee1.get_hours(), "hours worked at a rate of",
          myEmployee1.get_rate(), "per hour.")


if __name__ == '__main__':
    main()
