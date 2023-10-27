import math

sin=math.sin
cos=math.cos
tan=math.tan
factorial=math.factorial
sqrt=math.sqrt

while True:
    op=input("enter op(+,-,*,/,sin,cos,tan,cot,factorial,sqrt) or exit:")

    if op =="exit":
        break

    if op =="+":
        a=int(input("please enter number 1:"))
        b=int(input("please enter number 2:"))
        print(a+b)

    if op =="-":
        a=int(input("please enter number 1:"))
        b=int(input("please enter number 2:"))
        print(a-b)

    if op =="*":
        a=int(input("please enter number 1:"))
        b=int(input("please enter number 2:"))
        print(a*b)

    if op =="/":
        a=int(input("please enter number 1:"))
        b=int(input("please enter number 2:"))
        if b==0:
            print("error")
        else:
            print(a/b)

    if op =="sin":
        a=int(input("enter a(degree):"))
        print(math.sin(math.radians(a)))

    if op =="cos":
        a=int(input("enter a(degree):"))
        print(math.cos(math.radians(a)))

    if op =="tan":
        a=int(input("enter a(degree):"))
        print(math.tan(math.radians(a)))

    if op =="cot":
        a=int(input("enter a(degree):"))
        b=math.tan(math.radians(a))
        print(1/b)

    if op =="factorial":
        a=int(input("enter a number:"))
        if a<0:
            print("error")
        else:
            print(math.factorial(a))
    
    if op =="sqrt":
        a=int(input("enter a number:"))
        if a<0:
            print("error")
        else:
            print(math.sqrt(a))
