#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lenovo
#
# Created:     18-12-2021
# Copyright:   (c) lenovo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
introString = "My name is Avani. My age is 12. I am studing in class 7th. I am studing in all Saints High School. I love arts and english."
#words = introString.split()
#print(words)
#phrases = introString.split(",")

#print(phrases)

#def greet(name):
    #print("hello,"+ name +".how are you?")

#greet('Avani')

f = open('test.txt','r')
#print(f.read())
f.close()

fileLines = f.readlines()
for line in fileLines:
    print(line)