#Q1)
def greet(name,age):
    print("Hello " + name + "! You are " + str(age) + " years old.")
#Q2)
def intro(name,cou="Pakistan"):
    print(f"My Name is {name} and i am from {cou}.")
#Q3)
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
#Q4)
def total(a,b,c):
    return a+b+c
#Q5)
def show_names(*names):
    for names in names:
        print(names)
#Q6)
def student_details(**info):
        for key, value in info.items():
            print(key + ":", value)
#Q7)
def display(*args,**kwargs):
    print("Positional:",args)
    print("Keyword:",kwargs)
#Q8)
def show_subjects(*subjects):
    print("The subjects are:",subjects)
#Q9)
def show_student(**data):
    for key, value in data.items():
        print(key + ":", value)
#Q10)
def order(item,quantity=1,*extras):
    print("Item:",item)
    print("Quantity:",quantity)
    print("Extras:",extras)

def main():
    #Q1)
    greet("Ali",22)
    #Q2)
    intro("Ali","United Kingdom")
    #Q3)
    student_info("Hina",21,"A")
    student_info(section="B",name="Zain",roll=18)
    #Q4)
    print(total(80,90,80))
    #Q5)
    show_names("Ali","Sara","Ahmed")
    #Q6)
    student_details(Name="Ali",Age=18,City="Lahore")
    #Q7)
    display("OOP","Python",topic="Functions",Level="Intermediate")
    #Q8)
    subjects =["Math","AI","DSA"]
    show_subjects(*subjects)
    #Q9)
    info={"Name":"Ali","Age":21,"City":"Lahore"}
    show_student(**info)
    #Q10)
    order("Pizza",2,"Extra Cheese","Cold Drink")
if __name__ == "__main__":
    main()