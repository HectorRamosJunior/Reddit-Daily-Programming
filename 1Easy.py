"""
Reddit Daily Programmer Easy Challenge 1
Hector Ramos
1/12/2016
"""

def returnUserInformation():
    name = raw_input("Please enter your name: ")
    age = raw_input("Please enter your age: ")
    username = raw_input("Please enter your username: ")

    s = "Your name is %s, you are %s years old" %(name, age)
    s += ", and your username is %s." %username

    print s

    open("1EasyLog.txt", "a").write(s)

returnUserInformation()