# def personalInfo(fname,lname):
#     print("first name=", fname)
#     print("last name=", lname)
    
# personalInfo("prashant", "jha")

# #keyword argument
# def personalInfo(fname,lname):
#     print("first name=", fname)
#     print("last name=", lname)
    
# fname="prashant"
# lname="jha"
# personalInfo(fname,lname)

# #default arguement
# def cityName(city):
#     print(city)
    
# cityName("mumbai")
# cityName("delhi")
# cityName("")


#variable length arguement
def studentNames(*name):
    print(name)
    
studentNames("prashant", "rahul","sandep", "ashish")


