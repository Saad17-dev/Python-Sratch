#If else Practice
#Q1)
num=int(input("please write the number you want to check"))
if num>0:
    print("The number is positive")
else:
    print("Invalid or number is -ve")
#Q2)
age=int(input("please write the age you want to check"))
if age>=18:
    print("yes! you can vote")
else:
    print("no! you can't vote")
#Q3)
number=int(input("please write the number to check odd/even"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Elif & Nested If Practice
#Q1)
Marks=int(input("please write the Marks"))
if Marks >= 90:
    print("A*")
elif Marks >= 80:
    print("B")
elif Marks >= 70:
    print("C")
else:
    print("Fail")
#Q2)
username= input("please write the username")
password= input("please write the password")
if username == "admin" and password == "":
    print("You are not logged in")
else:
    print("Invalid Login")
#For Loop Practice
#Q1)
for numbers in range(1,11):
    print(numbers)
#Q2)
for even_numbers in range(0,21,2):
    print(even_numbers)
#Q3)
table_number=int(input("Enter the number of which you want table"))
for table in range(1,11):
    print(table*table_number)
#Q4)
word=("python")
for letter in word:
    print(letter)
#While loop practice
#Q1)
count=1
while count<6:
    print(count)
    count=count+1
#Q2)
password="python123"
while True:
    user_input=input("enter the password:")
    if user_input == password:
        print("Access Granted")
        break
    else:
        print("Try Again")
#Q2)
count=1
total=0
while count<101:
    total=total+count
    count=count+1
    print(total)
#Bonus Challenge
#Q1)
num=int(input("please write the number "))
if num<10:
    print("The number is small")
elif 10<=num<=50:
    print("The number is medium")
else:
    print("The number is large")
#Q2)
Exit=False
while Exit==False:
    Select = int(input("Select Option"))
    if Select==1:
        print("Hello")
    elif Select==2:
        print("1,2,3,4,5")
    elif Select==3:
        Exit=True
        print("Goodbye")