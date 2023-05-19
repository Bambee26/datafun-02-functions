"""

Author: Bambee Garfield
Purpose: Module 2 Task 4

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
import statistics 
import sys
import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Descriptive: Univariant data

# describe relationships of dog and cats
dogs = [2, 3, 10, 4, 2, 8, 1, 6, 5, 2, 7, 2]
cats = [1, 2, 5, 2, 12, 3, 1, 8, 4, 2, 2, 1]

# if the lists are not the same size,
# log an error and quit the program
if len(dogs) != len(cats):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(dogs)}!={len(cats)}")
    quit()

# log the information 
# zero decimal places because you can't have part of a dog or cat

# find the mean
mean_dogs = statistics.mean(dogs)
mean_cats = statistics.mean(cats)
logger.info(f"The mean of dogs is {mean_dogs:.0f} and cats is {mean_cats:.0f}.")

# find the median 
median_dogs = statistics.median(dogs)
median_cats = statistics.median(cats)
logger.info(f"The median of dogs is {median_dogs:.0f} and cats is {median_cats:.0f}.")

# find the mode
mode_dogs = statistics.mode(dogs)
mode_cats = statistics.mode(cats)
logger.info(f"The mode of dogs is {mode_dogs:.0f} and cats is {mode_cats:.0f}.")

# find the variance
var_dogs = statistics.variance(dogs)
var_cats = statistics.variance(cats)
logger.info(f"The variance of dogs is {var_dogs:.0f} and cats is {var_cats:.0f}.")

# find the standard deviation
stdev_dogs = statistics.stdev(dogs)
stdev_cats = statistics.stdev(cats)
logger.info(f"The standard deviation of dogs is {stdev_dogs:.0f} and cats is {stdev_cats:.0f}.")

# find the smallest
smallest_dogs = min(dogs)
smallest_cats = min(cats)
logger.info(f"The smallest number of dogs is {smallest_dogs} and cats is {smallest_cats:.0f}.")

#find the largest
largest_dogs = max(dogs)
largest_cats = max(cats)
logger.info(f"The largest number of dogs is {largest_dogs:.0f} and cats is {largest_cats:.0f}.")

#find the range
range_dogs = largest_dogs - smallest_dogs
range_cats = largest_cats - smallest_cats
logger.info(f"The range in the number of dogs is {range_dogs:.0f} and cats {range_cats:.0f}.")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())