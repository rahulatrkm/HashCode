# reading the input file
file = open('a_example.in', 'r')
line = file.readlines()
[r, c, mn, mx] = list(map(int, line[0].split()))
# initializing the 2d array
temp = [[ 0 for i in range(c) ] for j in range(r) ]
countT = 0
counM = 0
# read the pizza array
pizza = []
for i in range(r):
    temp = list(line[i+1].rstrip())
    pizza.append(temp)
    countT += temp.count('T')
countM = r*c - countT
if countT > countM:
    print(cutSlices(pizza, temp, 'M'))
else:
    print(cutSlices(pizza, temp, 'M'))

def cutSlices(pizza, temp, less):
    for 
