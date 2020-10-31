# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:46:26 2020

@author: matthew
"""
#this program is for extracting numbers from a text file and averaging them together.
#the numbers are drawn from lines referring to "X-DSPAM-Confidence"
#the resulting average is the averge confidence score

#accessing file
file_name = input("Enter file name: ")
fh = open(file_name)

#extracting lines containing relevant data
def line_locator():
    line_array = []
    count = 0
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            count = count + 1
            line = line.rstrip()
            line_array.append(line)
    return line_array
l_list = line_locator()
print(l_list)

#finding the index for the first number in each line of data
def number_locator(array):
    first_num_pos = array[0].find('0')
    return first_num_pos
f_index = number_locator(l_list)
print(f_index)

#extracting numbers from the lines of text
def extract_nums(array):
    number_array = []
    for i in array:
        number_array.append(i[f_index:])
    return number_array
n_list = extract_nums(l_list)
print(n_list)

#convert numbers into floats and average them together
def average_nums(array):
    total = 0
    count = 0
    for i in array:
        count = count + 1
        total = total + float(i)
    mean = total / count 
    return mean
average = average_nums(n_list)
print("Average spam confidence:", average)