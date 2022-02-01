"""
lab 12 - Fill in the parts for the class
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

class Computer:
    """ computer class definition """
    def __init__(self, processor, ram):
        # creating an instance variable name processor
        # and assigning it the value of the parameter named processor
        self.processor = processor

        # create an instance variable named ram
        # and assign it the value of the parameter named ram
        self.ram = ram

    def set_processor(self, processor):
        """ defining a setter for the processor instance variable """
        self.processor = processor

    def set_ram(self, ram):
        """ define a setter for the ram instance variable """
        self.ram = ram

    def get_processor(self):
        """ defining a getter for the processor instance variable """
        return self.processor

    def get_ram(self):
        """ define a getter for the ram instance variable """
        return self.ram


# Construct a computer object
myComputer = Computer("Intel",100)

# Use getters to display the processor and ram for the computer you constructed
print("The processor is",myComputer.get_processor(),"with memory",myComputer.get_ram())   
