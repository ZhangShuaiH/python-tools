import os,random

size = 10
min = 10
max = 100

file = open('array.txt', 'w')
array = []
for i in range(len):
    array.append(random.randint(min, max))
file.write(str(array))
