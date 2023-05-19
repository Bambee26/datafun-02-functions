"""
Purpose: illlustrate some built-in functions, conditions, and branching.

Always start your file with a docstring.

Each file is a module in Python.
The name of the module is the name of the file without the extension.

"""

import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

print("Hello! Let's calculate the amount of water your pet drinks in a day.")
print()

bowl_width = input("Tell me the width of your pet's water bowl: ")
print()
bowl_height = input("Thanks, now tell me how tall the bowl is: ")
print()
bowl_refills = input("How many times per day do you refill the bowl?: ")
print()

# convert strings to numbers
bowl_width = float(bowl_width)
bowl_height = float(bowl_height)
bowl_refills = int(bowl_refills)

logger.info(f"Width = {bowl_width}")
logger.info(f"Height = {bowl_height}")
logger.info(f"Refills = {bowl_refills}")

# calculate the radius of bowl
bowl_radius = round((bowl_width / 2), 2)

# caclulate the volume in inches cubed 
bowl_volume = round((math.pi * (bowl_radius) ** 2 * (bowl_height)), 2)

# calculate the volume by gallon (1 gallon = 231 inches cubed)
bowl_gal = round((bowl_volume / 231), 2)

# caclulate the volume in ounces (1 gallon = 128 ounces)
bowl_ounces = round((bowl_gal * 128), 2)

# find daily amount in ounces
daily_total = round((bowl_refills * bowl_ounces), 2)

# print the results
logger.info(f"We need the bowl's radius to calculate it's volume. The radius is {bowl_radius}.")
logger.info(f"The volume of the bowl in inches cubed is {bowl_volume}\".")
logger.info(f"The bowl's volume in gallons is {bowl_gal}.")
logger.info(f"The bowl's volume in ounces is {bowl_ounces}.")
logger.info(f"You refill the bowl {bowl_refills} time(s) per day.")
logger.info(f"Your pet drinks {daily_total} ounces of water per day.")

# conditions and branching

utterance1 = "That's at least 3 jugs of milk."
utterance2 = "That's like a large bottle of soda"
utterance3 = "You should check on your pet, that's not much water."  
temp_freezing = 0

if daily_total >= 384:
    logger.info(utterance1)
elif daily_total < 384 and daily_total > 128:
    logger.info(utterance2)
else:
    logger.info(utterance3)


# ask more

logger.info("Script complete. See log file for details.")

# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())