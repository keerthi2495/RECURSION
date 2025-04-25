def flower(a):
    if(a==4):
        return
    print(a+10,end=" ")
    flower(a+1)
    print(a,end=" ")
flower(1)

print("_________________________________")

def raju(a):
    if(a==1):
        return
    raju(a-1)
    print("Hai")
    raju(a-1)
raju(5)


def abc(a):
    if a==4:
        return
    a+=1
    abc(a)
    print("CSE",end=" ")
    abc(a)
    print("MECH",end=" ")
def main():
    num="12"
    for a in num:
        print()
        abc(int(a))
main()

print("________________________")


def ab(n):
    if n==1:
        return 2
    b=ab(n-1)
    print("Hai",end=" ")
    return b+1
print(ab(5))    
    

