# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:07:58 2020

@author: Matthew
"""

#open file
file_n = input("Enter file name: ")
try:
    file_h = open(file_n)
except:
    print("File not found")
    quit()

#read the contents of the file and extract relevant lines
def file_reader(doc):
    data = []
    for line in doc:
        if line.startswith("From "):
            data.append(line)
    return data
contents = file_reader(file_h)
#print(contents)

#cleaning the extracted dataset
def data_cleaner(data):
    cleaned_data = []
    for i in data:
        cleaned_data.append(i.rstrip('\n'))
    return cleaned_data
clean_data = data_cleaner(contents)
#print(clean_data)

#splitting the data 
def data_splitter(data):
    split = []
    for i in data:
        split.append(i.split())
    return split
split_data = data_splitter(clean_data)
#print(split_data)

#collecting time stamps
def separate_times(data):
    times = []
    for i in data:
        times.append(i[5])
    return times
time_stamps = separate_times(split_data)
#print(time_stamps)

#split time stamps and collect hours
def split_times(data):
    times = []
    for i in data:
        times.append(i.split(':'))
    return times
split_time_stamps = split_times(time_stamps)
#print(split_time_stamps)

def collect_hours(data):
    hour = []
    for i in data:
        hour.append(i[0])
    return hour
hours = collect_hours(split_time_stamps)
#print(hours)

#create a histogram wherein dictionary key refers to hours and value refers to frequency
def generate_dictionary(data):
    dictionary = dict()
    for i in data:
        dictionary[i] = dictionary.get(i, 0) + 1
    return dictionary
frequency = generate_dictionary(hours)
#print(frequency)

#convert dictionary to tuples and sort
frequency_tuples = sorted(frequency.items())
for k, v in frequency_tuples:
    print(k, v)
#print(frequency_tuples)



