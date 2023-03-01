#Write a program to check if two strings are a rotation of each other?

def are_rotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    
    if size1 != size2:
        return 0
    
    temp = string1 + string1
    
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

string1 = 'ABCDEF'
string2 = 'DEFABC'

if are_rotations(string1, string2):
    print ('The Strings are rotations of each other')
else:
    print ('The Strings are not rotations of each other')