# there are 4 type of function arguments
    #  1. keyword arguments
    #  2.defoult arguments
    #  3.variable-length arguments
    #  4.requered arguments

# default arguments:-
def average(a=9, b=1):
    print("the average is",(a+b)/2)

average(1+5)

#this is also a defult argument:-
def name(fname,mname ="jhon", lname = "whatson"):
    print("hello,",fname, mname, lname)
name("amy", "agarwal")
name("Aninda","","Betal")



# keyword arguments:-  (you can change the order)
def avarage1(a, b):
    print("the avarage is: ",(a+b)/2)

avarage1(b=20, a=40)

 
 

#required arguments  (must be give one value)                                                                                             
def box3(a, b, c=2):
   print("the avarage number is: ", (a+b)/c)

box3(4, 10)


# Variable-length arguments
def box4(*numbers):
   sum=0
   for sum in numbers:
      sum= sum+ 1
   print("tihe avarage is: ", sum/len(numbers))

 
box4(10,11, 33, 44)