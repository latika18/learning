#! usr/bin/python

#Add a get variable in url like : www.lashp3.com/filename?name=rob
#following code will print the get variable on screen

print('content-type:text/html')
print("")

import cgi
form = cgi.FieldStorage()

print(form.getvalue("name"))
