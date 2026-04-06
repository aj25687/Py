print ("hello")

#forloops

num=4
for i in range(0,num):
    print(i)
#like java foreach

list = ["a","b","c"]
for x in list:
    print(x)

alpha = "abcd"
for x in alpha:
    print(x)

print(len(list))

mw = 0
while (mw < 6):
    mw= mw+1
    print("hellow")

n=0
while(True):
    print("test num",n)
    n = n+1
    if(n>3):
        break

print("done")

for i in range(1,5):
    for j in range(i):
        print(i, end=' ')

print()
    
arr = [0]*5
print(arr)
for i in range(len(arr)):
    arr[i]=i
print(arr)

grid = [[0]*5]*2 #bad dont do this makes two rows identical to each other
grid = [[0 for _ in range(5)] for _ in range(2)]
print(grid)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = (i+1)*(1+j)
print(grid)