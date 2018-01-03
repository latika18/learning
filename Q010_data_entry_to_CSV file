##Make a data entry shell script. It asks for 3 information, Name, phone number, and email address.
##It keeps on executing till user enters exit (in any case), or exits forcefully.
##Write all the data collected into a CSV file. Every combination of Name, phone number,
##and email address entered go into a single row.

##input details
    
i = 0
list =  ['Name' , 'Phone_Number' , 'Email_Address']
details = [list]
while i >=0:
    Name = raw_input("Enter your Name: ")
    if Name == 'exit':
        break
    Phone_Number = raw_input ("Enter your Phone Number: ")
    if Phone_Number == 'exit':
        break
    Email_Address = raw_input ("Enter your email address")
    if Email_Address == 'exit':
        break
    d = [Name , Phone_Number , Email_Address]
    details.append(d)
    i = i+1

#write this data in format preffered by excel
import csv
with open('details.csv ','wb') as f:
    writer = csv.writer(f)
    writer.writerows(details)
with open('details.csv', 'r')as f:
    for line in f:
        print line








