# Workout Tracker - Marshall Ferguson - 7/2020

# Imports

import csv
import matplotlib.pyplot as plt 

# TODO - take input from the command line
    # TODO - ask the user the name of exercise, sets, reps, and weight
    # TODO - calculate the volume lifted, the total sets, and total reps

print("Welcome to the Workout Tracker!")
output_file = open(".\\workout_data.csv", "a", newline="")
output_writer = csv.writer(output_file)
print("Please enter your information for your workout.")
while True:
    user_input = input("Enter 'done' when you are done adding workout information, or press enter to continue.\n")
    if user_input.lower() != "done":
        name = input("Please enter the name of the exercise you want to add next:     ")
        sets = input("How many sets did you perform?     ")
        sets = int(sets)
        reps = input("How many reps did you perform each set?     ")
        reps = int(reps)
        weight = input("How much weight did you lift each rep? (in lbs)     ")
        weight = int(weight)
        total_reps = reps * sets
        volume = total_reps * weight
        print("You performed {} sets of {} reps of {} at {} lbs".format(sets, reps, name, weight))
        print("You performed a total of {} reps and lifted a total volume of {} lbs".format(total_reps, volume))
        output_writer.writerow([name, sets, reps, weight, total_reps, volume])
    else:
        break

# TODO - output to a csv file

output_file.close()

# TODO - visualize data