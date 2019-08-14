#! usr/bin/python

print('content-type:text/html')
print("")

import cgi
form = cgi.FieldStorage()

if "guess" in form:
  guess = form.getvalue("guess")
else:
  guess = ""

print("<h1>Are You ready to play MasterMind</h1>")
print("<p>I have chosen a 4-digit number. Can you guess it</p>")
print("<form>")
print('<input type="text" name="guess" value="guess">')
print('<input type="Submit" value="Guess!">')
print("</form>")
print(guess)
