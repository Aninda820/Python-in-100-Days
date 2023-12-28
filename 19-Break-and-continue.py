# break and continue

for n in range(15):
    print("5 x",n,"=",(5*n))
    if(n==10):
        break
print("skip the next lines")




for n in range(15):
    if(n==10):
        print("now i'm out from loop")
        continue
    print("4 x",n,"=",(4*n))





for i in range(1,12):
    print(5, "*", i, "=", 5*(i))
    if(i==10):
        break
print("This is the table of 5")





for x in range(1, 12):
     print(5, "*", x, "=", 5*(x))
     if(x==10):
         print("skip the iteration!")
         continue
     
