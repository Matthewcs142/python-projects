# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:59:03 2020

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
        if line.startswith("From") and not line.startswith("From:"):
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

#printing the list of emails and counting the total number of addresses
count = 0
for i in email_addresses:
   count = count + 1
   print(i)
print("There were", count, "lines in the file with From as the first word")
