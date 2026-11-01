#Inbuilt modules
#They come pre-installed with the intrepreter 
import math
print(math.sqrt(4))

import datetime
print(datetime.datetime.now())

#Find other three inbuilt modules and what they do.Have an example of each
print("============")
#Import random module prints a random number betweem the specified range
import random
print(random.randint(1,10))

#Import os module  prints the current working directory
import os
print(os.getcwd())

#Import sys module prints the version of python installed in the system
import sys
print(sys.version)

#Import statistics module prints the required statistics of a given list of numbers
import statistics
print(statistics.variance([1, 2,5, 3, 4, 5]))

#Import json module prints the json representation of a given python dictionary
import json
data = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(json_data)

#Import re module prints the matched pattern in a given string
import re
pattern = r"\d+"
string = "There are 5 apples and 4oranges."
matches = re.findall(pattern, string)
print(matches)

#Import calendar module prints the calendar of a given year
import calendar
print(calendar.calendar(2026))

#Import Collections module prints the count of each element in a given list
import collections
list1 = [1, 2, 3, 4, 5, 1, 2, 3]
counter = collections.Counter(list1)
print(counter)