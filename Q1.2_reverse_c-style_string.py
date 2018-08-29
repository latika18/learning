1.2 Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)

def reverse_string(string1):
    string1=string1[::-1]
    return string1[1:]

print reverse_string('1234 ')
