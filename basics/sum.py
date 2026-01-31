"""first = int(input("ENTER first number :"))
second = int(input("second number :"))

sum =  first+second
print("sum is :", sum)"""

"""length = int(input("enter length :"))
width = int(input("enter width :"))

area = length*width
print("area of a rectangle is :", area)"""

"""number = int(input("enter a number :"))
square = number*number
cube = number*number*number
print("The square is ", square, "and cube is :",cube)"""

"""number = int(input("take a number :"))
if number<0 :
    print("the number is negetive")
elif number==0 :
    print("number is zero")
else :
    print("the numvber is positive")"""



number = int(input("enter a number :"))
print(f"Numbers between 1 and {number} that are divisible by 3:")
for i in range(1,number+1) :
    if i%3==0 :
        print(i)

    