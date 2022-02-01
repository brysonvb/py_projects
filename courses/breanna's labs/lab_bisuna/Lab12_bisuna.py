"""
Lab 12 - Fill in the parts for the class
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

class computer:
    def __init__(self, processor, ram):
        # creating an instance variable name processor
        # and assigning it the value of the parameter named processor
        self.processor = processor
        
        # create an instance variable named ram
        # and assign it the value of the parameter named ram
        self.ram = ram


    # defining a setter for the processor instance variable
    def set_processor(self, processor):
        self.processor = processor

    # define a setter for the ram instance variable
    def set_ram(self, ram):
        self.ram = ram

    # defining a getter for the processor instance variable
    def get_processor(self):
        return self.processor

    # define a getter for the ram instance variable
    def get_ram(self):
        return self.ram


# Construct a computer object
myComputer = computer("Intel",100)

# Use getters to display the processor and ram for the computer you constructed
print("The processor is",myComputer.get_processor(),"with memory",myComputer.get_ram())


    
