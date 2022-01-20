

from numpy import maximum


a = int(input("enter first number\n"))
b = int(input("enter second number\n"))
maxNum = max(a, b)
while(True):
    print(f"IF {maxNum % a == 0} {maxNum % b == 0}")
    if(maxNum % a == 0 and maxNum % b == 0):
        print(f"condi stis {maxNum}")
        break
    maxNum = maxNum + 1
    print(maxNum)
print(f"The LCM of {a} and {b} is {maxNum}")
