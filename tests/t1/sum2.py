# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
numbers=[]
argument=True
while argument:
    listnum=input("Please insert numbers here: ")
    if "-1" in listnum:
        argument=False
        print(sum(numbers))
    else:
        numbers.append(int(listnum))