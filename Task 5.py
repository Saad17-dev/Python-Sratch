#Q1)
for num in range(1,10):
    if num ==6:
        break
    print(num)
print("Loop Ended")
#Q2)
for num in range(1,10):
    if num ==4 or num ==7:
        continue
    print(num)
#Q3)
for num in range(1,5):
    if num==1 or num==2 or num==3 or num==4:
        pass
    print(num)
print("See Nothing Happend")
#Q4)
while True:
    num=int(input("PLease enter the number"))
    if num==0:
        print("loop ended")
        break
#Q5)
for num in range(1,20):
    if num%2==0:
        continue
    print(num)
#Q6)
"""while True:
    name=input("Enter name")
    if name[0]=='a':
        continue
    print(name)"""
#Q7)
for num in range(1,10):
    if num%3==0:
        continue
    elif num==8:
        break
    print(num)
