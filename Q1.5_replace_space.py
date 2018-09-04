#Q1.5 Write a method to replace all space in a string with "%20"

def replace_space(string1):
    for c in string1:
        if c == " ":
            string1 = string1.replace(c,"%20")
    return string1

print replace_space("This is a plain text")

