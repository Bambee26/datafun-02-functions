'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to dog walking. 

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

Dog walking adds:

- a location attribute

'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from numeric_series import NumericSeries

# From the util_datafun_logger module, import the setup_logger function
from util_datafun_logger import setup_logger


class NumericDogWalkSeries(NumericSeries):
    """
    A class representing a numeric series customized for dog walking data.

    (Additional) Attributes:
       location (string): the location where the data was collected
    """

    def __init__(self, name, units, data, location):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            location (str): the location where the data was collected

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.location = location

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericDogWalkSeries with name={self.name}, units={self.units}, location={self.location}, and {len(self.data)} data points: {self.data}"
        return str




if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # First, setup logging
    logger, logname = setup_logger(__file__)

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Dog #1 Walks"
    units1 = "miles"
    data1 = [2.8, 1.4, 2.4, 1.3, 0.8]
    loc = "Neighborhood"

    object1 = NumericDogWalkSeries(name1, units1, data1, loc)

  
    name2 = "Dog #2 walks"
    units2 = "miles"
    data2 = [1.2, 2.2, 3.0, 0.4, 2.4, 3.1, 1.3]
    loc2 = "Park"

    object2 = NumericDogWalkSeries(name2, units2, data2, loc2)

    
    # Create another object 

    # use range() to create a list of values from 65 to 78
    # list() converts the range object to a list
    # range() is a generator - it creates a sequence of numbers without storing them in memory
    # The arguments in range are from (inclusive) and to (exclusive)
    data3 = list(range(1, 4))
    name3 = "Dog #3 Walks"
    units3 = "miles"
    loc3 = "Neighborhood and park"

    object3 = NumericDogWalkSeries(name3, units3, data3, loc3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]

    # Loop through our objects and get some statistics
    # Rather than using a built-in function and passing in our data
    # we call methods directly on our objects
    # Why? It's just another way to organize and reuse code. 
    # We encapusulate (wrap up) the attributes and associated methods into a resuable class. 
    # Write the class once, and use it many times. 
    # We'll see this a lot when we use dataframes to hold tables of data. 
    # Many popular libraries provide reusuable classes. 
    # It's a powerful way to organize code when dealing with many objects of the same type.

    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count():0.2f}")
        logger.info(f"Sum: {object.sum():0.2f}")
        logger.info(f"Mean: {object.mean():0.2f}")
        logger.info(f"Median: {object.median():0.2f}")
        logger.info("------------------")

    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
      print(file_wrapper.read())