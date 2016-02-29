# write a program that reads in 10 numbers, then prints the sum of those
numbers=[]
for i in range(10):
    listnum=int(input("Please insert numbers here: "))
    numbers.append(listnum)
print(sum(numbers))