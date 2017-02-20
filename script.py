#
#This script is for eduactional purposes
#

def hello(a):
    for n in range(a):
        print ("hello world")

hello(300)

#there is another way to spam ones console
#by multiplying the value of the print statement:

print ("hello world " * 300)

#alternative way for a loop
#this loop asks your to enter "your name"
#if any other input is given, the loop continues to ask you to
#enter "your name"

def world():
    while True:
        print ("Please enter your name: ")
        name = input()
        if name == "your name":
            break
    print ("thank you")
