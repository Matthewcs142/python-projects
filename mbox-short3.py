# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:29:27 2020

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

#collecting emails
def separate_emails(data):
    emails = []
    for i in data:
        emails.append(i[1])
    return emails
email_addresses = separate_emails(split_data)
#print(email_addresses)

#create a histogram wherein dictionary key refers to email and value refers to frequency
def generate_dictionary(data):
    dictionary = dict()
    for i in data:
        dictionary[i] = dictionary.get(i, 0) + 1
    return dictionary
frequency = generate_dictionary(email_addresses)
#print(frequency)

#finding the most frequent email address
most_frequent_email = None
count = None

frequency = frequency.items()
for x, y in frequency:
    if most_frequent_email == None or y > count:
        most_frequent_email = x
        count = y
print(most_frequent_email, count)
