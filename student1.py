class student:
    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
    def accept(self,name,rollno,marks1,marks2):
        ob=student(name,rollno,marks1,marks2)
        list.append(ob)
    def display(self,ob):
        print("name :",ob.name)
        print("rollno :",ob.rollno)
        print("marks1:",ob.m1)
        print("marks2:",ob.m2)
        print("\n")
    def seaarch (self,rn):
        for i in range (list.__len__()):
            if (list[i].rollno==rn):
                return i
    def delete(self,rn):
        i=object.search(rn)  
        del list[i]
    def update(self,rn,no):
        i = object.search(rn) 
        roll=no
        list[i].rollno=roll
list=[]
object=student('',0,0,0)
print("\n operations used,")
print("\n1.accept student details\n2.display student details\n3.search details of a student\n4.delete of student\n5.update student details\n6.exit")
object.accept("lata",1,100,100)
object.accept("khyati",2,90,90)
object.accept("laxmi",3,80,80)
print("\n")
print("\n list of studentd\n")
for i in range (list.__len__()):
    object.display(list[i])
print("\n student found,")
s=object.search(2)
object.display(list[s])
object.display(list[s])
 

object.delete(2)
print(list.__len__())
print("List after deletion")
for i in range(list.__len__()):
    object.display(list[i])
 

object.update(3, 2)
print(list.__len__())
print("List after updation")
for i in range(list.__len__()):
    object.display(list[i])
 

print("Thank You !")
