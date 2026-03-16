# mylist = ["prashnat", "aashish", "komal" , "ankush", "sandip" , 60.43 , 77]
# newlist = mylist.copy()
# print(mylist)
# print(newlist)

# mylist= [['prashant','jha'], [83.4], [440020, "yyy"]]
# print("example of multidimentional list")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])


# list1=["prashnat", "jha"]
# print(list1*2)
# list2=[50,25.50]
# print(list1+list2*2)

# list2=[50,25.50, 'prashant']
# del list2[1]
# print(list2)
# # del list2  deleting the whole list
# list2.clear()
# print(list2)


# name="prashant"
# print(name)
# mylist= list(name)  #typecasting
# print(mylist)

# #sorting example
# mylist=[44,22,77,0,9,88]
# mylist.sort()
# print(mylist)
# mylist.reverse()
# #mylist.sort(reverse+True)
# print(mylist)

#default order for sorting number is ascending order
#default sorting order for alphabet is alphabetical order 

# math = 10 
# phy = 10
# eng = 40
# print(id(math)) #address of variable
# print(id(phy))
# print(id(eng))

# #aliasing means assigning one variable reference to another variable 
# mylist=[44,22,0,9,88]
# newlist =mylist
# print(id(mylist))
# print(id(newlist))

#looping 
# # 2 types of special operators used in python, membership operator--in , not in
# name= 'prashnat'
# print('Z' in name)
# print('Z' not in name)

# for i in range(1,10,3):
#     print(i)

# for i in range(5,0,-1):
#     print(i)
    
# for i in range(1,11):
#     print(i*2, " ", i*3, " ", i*4, " ", i*5," ",i*6," ",i*7," ",i*8," ",i*9," ", i*10)

# #WAP to accept any digit and check that pos ,neg, zero
# no= int(input('enter any digit: '))
# if no>0:
#     print("positive")
# if no<0:
#     print("negative")
    
# if no==0:
#     print("zero")

# #WAP to accpet days and check the working days and weeknd
# days = input("enter name of day: ")
# if days == "saturday" or "sunday" or "SATURDAY" or "SUNDAY":
#     print("weeknd")
    
# else:
#     print("working day")

# #WAP to acceept three paper marks and calculate total, percentage and
# #if percentage is greater then equal to 60 then he/she is eligible for placement
# phy = int(input("enter the physics marks: "))
# math = int(input("enter the maths marks: "))
# chem= int(input("enter the chemistry marks: "))
# total = phy+math+chem
# per=total/3.0
# print(per)
# if per>=60:
#     print("eligible for placement")
    
# else:
#     print("not eligible for placement")


# #WAP to accept five diffrent value in 5 diffrent variable and check maximum value and print by using simple if statement
# a=int(input("enter 1st number: "))
# b=int(input("enter 2nd number: "))
# c=int(input("enter 3rd number: "))
# d=int(input("enter 4th number: "))
# e=int(input("enter 5th number: "))

# if a>b and a>c and a>d and a>e:
#     print("a is the greatests")
    
# if b>a and b>c and b>d and b>e and a>e:
#     print("b is the greatests")
    
# if c>a and c>b and c>d and c>e :
#     print("c is the greatests")
    
# if d>a and d>c and d>b and d>e:
#     print("d is the greatests")
    
# if e>a and e>c and e>b and e>d:
#     print("e is the greatests number")

    

    



































