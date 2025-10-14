#Q1)
animals=["cat","dog","rabbit"]
print(animals[1])
animals.append("parrot")
print(animals)
animals[1]= "lion"
print(animals)
print(len(animals))
#Q2)
colors=("red","green","blue")
print(colors[1])
#colors[0]="yellow"
#TypeError: 'tuple' object does not support item assignment
print(len(colors))
#Q3)
numbers={1,2,3,3}
print(numbers)
numbers.add(4)
print(numbers)
numbers.remove(3)
print(numbers)
numbers_to_check = 2
if numbers_to_check in numbers:
    print(f"{numbers_to_check} is not in set")
else:
    print(f"{numbers_to_check} is not in set")
#Q4)
student={"name":"John","age":"12"}
print(student)
student["city"]="Silicon Valley"
print(student)
student["age"]=56
print(student)
del student["city"]
print(student)
