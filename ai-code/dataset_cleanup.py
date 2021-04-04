import pandas
import numpy
import os

# The original csv file needed some cleaning up! I did that below,
# using Python

dataset_loaded = pandas.read_csv(os.path.join(os.getcwd(), "ai-code/insurance.csv"))
print(dataset_loaded["smoker"][1337])
location_list = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]

# A neural network understands numbers better than letters,
# so I hear I used "one-hot encoding"- I replace text categories
# with numbers (for example, male/female becomes 0/1).
for iterator in range(1338):
    if dataset_loaded["smoker"][iterator] == "yes":
        dataset_loaded["smoker"][iterator] = 1
    else:
        dataset_loaded["smoker"][iterator] = 0
    if dataset_loaded["sex"][iterator] == "female":
        dataset_loaded["sex"][iterator] = 1
    else:
        dataset_loaded["sex"][iterator] = 0
    # We'll replace the location with numerical 
    # values from 0-7.
    location = dataset_loaded["region"][iterator]
    dataset_loaded["region"][iterator] = location_list.index(location)
    
dataset_loaded.to_csv("insurance_cleaned.csv")