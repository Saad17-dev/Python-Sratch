#Q1)
def Printing():
    print("hello world")
#Q2)
def Greet(name):
    print("Hi", name)
#Q3)
def Squarenumber(num):
    sq=num*num
    print(sq)
#Q4)
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
#Q5)
def add_numbers(num1, num2,num3):
    return num1+num2+num3
#Q6)
def maximum(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
#Q7)
def average(num1, num2, num3):
        avg=num1+num2+num3
        return avg/3
def main():
    #Q1)
    Printing()
    #Q2)
    Greet("Franklin")
    #Q3)
    Squarenumber(5)
    #Q4)
    num=8
    if is_even(num):
        print(num,"is even")
    else:
        print(num,"is odd")
    #Q5)
    result=add_numbers(21,43,256)
    print("the sum is:",result)
    #Q6)
    max=maximum(21,67)
    print("the max is:",max)

    #Q7)
    avg=average(11,7,3)
    print("the average is:",avg)
if __name__=="__main__":
        main()
