import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import csv
import os 
from random import SystemRandom as sys_random

# variables
number_to_generate = 50000000
board_squares = 40

# Random number generator to simulate two dice throws
# range: [2,12]
# mod %40 to get the final set location after the dice row
cryptogen = sys_random()
dice_throw_list = [cryptogen.randint(2,12) for i in range(number_to_generate)]
# print (dice_throw_list)

# suppose only one player
step_sum = 0
board_hotness = {}

# initialize dictionary board_hotness
for index in range (0,board_squares,1):
    board_hotness.setdefault(index, 0)
# print (board_hotness)

for dice_index, dice_result in enumerate (dice_throw_list):
    # print ("dice_index={}, dice_result={}".format(dice_index, dice_result))
    step_sum += dice_result
    board_location = step_sum % board_squares
    # print ("board_location={}".format(board_location))
    board_hotness[board_location] += 1
    # print ("board_hotness={}".format(board_hotness))

print (board_hotness)

# find highest and lowest probability location
key_max = max(board_hotness.keys(), key=(lambda k: board_hotness[k]))
key_min = min(board_hotness.keys(), key=(lambda k: board_hotness[k]))
print('Maximum Value: ',key_max)
print('Minimum Value: ',key_min)

plt.plot(board_hotness.keys(), board_hotness.values())
plt.show(block=False)
input('press <ENTER> to continue')

# cwd=os.getcwd()
# print (cwd)
# file_path=os.path.join(cwd, 'individual_stocks_5yr/AAPL_data.csv')
# with open(file_path, 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print (row)